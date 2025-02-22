from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import fitz

embedder = SentenceTransformer("all-MiniLM-L6-v2")

documents =[]

# documents = [
#     "Places to eat in Bengaluru are MTR for authentic South Indian breakfast, Truffles for amazing burgers, and Vidyarthi Bhavan for legendary dosas.",
#     "Places to explore nature in Bengaluru are Lalbagh Botanical Garden, Cubbon Park, and Turahalli Forest for a mix of greenery and outdoor fun.",
#     "Historical places to visit in Bengaluru are Bangalore Palace, Tipu Sultan's Summer Palace, and the Bangalore Fort.",
#     "Cafes to hang out with friends in Bengaluru are Third Wave Coffee Roasters, Dyu Art Café, and Matteo Coffea.",
#     "Rooftop restaurants in Bengaluru are Ebony, High Ultra Lounge, and Skyye for stunning views and great food.",
#     "street food in Bengaluru are VV Puram Food Street, Shivaji Nagar, and Rameshwaram Café.",
#     "weekend getaways from Bengaluru are Nandi Hills, Mysore, and Coorg for a quick break from the city.",
#     "shopping areas in Bengaluru are Commercial Street, Brigade Road, and Chickpet for a mix of fashion, brands, and traditional finds."
# ]

try:
    
    doc = fitz.open("tour-guide.pdf")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        documents.append(page.get_text())

    doc.close()

except Exception as e:
    print(f"Error reading PDF: {e}")
    exit(0)


document_embeddings = embedder.encode(documents)

dim = document_embeddings.shape[1] 
index = faiss.IndexFlatL2(dim)  
index.add(np.array(document_embeddings))  

llm = OllamaLLM(model="mistral", temperature=0.2)

prompt = """
You are a knowledgeable and friendly travel planner. Using the provided context, create a detailed 3 day itinerary for a trip to {place}. 

For each day, include:
- Morning: A popular attraction or activity.
- Afternoon: A recommended restaurant or café for lunch and another attraction or experience.
- Evening: A dinner spot and a relaxing or cultural activity.

If the context does not mention {place}, kindly state that you do not have enough information and suggest general travel planning tips instead.

Context:
{context}

Make the itinerary engaging, practical, and fun!
"""


prompt_template = PromptTemplate(
    input_variables=["context", "place"],
    template=prompt
)


def rag_response(query, top_k=2):
    query_embedding = embedder.encode([query])

    distances, indices = index.search(np.array(query_embedding), k=top_k)
    retrieved_docs = [documents[i] for i in indices[0]]

    context = "\n".join(retrieved_docs)

    final_prompt = prompt_template.format(context=context, place=query)

    print("\n\n\n--- Retrieved Documents ---")
    for doc in retrieved_docs:
        print(f"- {doc}")
    
    print("\n\n")
    

    response = llm.predict(final_prompt)
    return retrieved_docs, final_prompt, response

print("Welcome to WanderPy, your Friendly Travel Planner !!! \n\n")
print("Type 'exit' or 'quit' to stop the conversation.\n")
input_query = input("User: The place I want to visit is: ")
while True:
    if input_query.lower() in ["exit", "quit"]:
        break

    docs, prompt_used, answer = rag_response(input_query, top_k=4)

    print(f"WanderPy bot: {answer}")
    input_query = input("User: ")

