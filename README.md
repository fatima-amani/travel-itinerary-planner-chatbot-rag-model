# 🧭 WanderPy: AI-Powered Travel Itinerary Planner

WanderPy is a smart chatbot that uses Retrieval-Augmented Generation (RAG) to plan personalized travel itineraries. It combines contextual knowledge from a PDF travel guide with the power of AI (using Ollama + Mistral) to suggest practical, engaging travel plans.

## ✨ Features

* 📍 **Context-Aware Itineraries**: Reads from a travel guide PDF to tailor suggestions
* 🧠 **RAG-Based Intelligence**: Combines semantic search and LLMs for accurate, relevant plans
* 🤖 **Conversational Interface**: Interact naturally and receive multi-day trip suggestions
* 📚 **PDF Document Integration**: Easily customize the travel context by replacing the guide

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/fatima-amani/travel-itinerary-planner-chatbot-rag-model.git
cd travel-itinerary-planner-chatbot-rag-model
```

### Set Up a Virtual Environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/MacOS
source venv/bin/activate  
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 📄 Required Files

* `tour-guide.pdf`: Place your PDF travel guide in the project root. This will be parsed to retrieve information used in itinerary creation.

## 🚀 Usage

Run the chatbot:

```bash
python travel_itinerary_rag_llm.py
```

Then interact with the bot:

```
Welcome to WanderPy, your Friendly Travel Planner !!!
User: The place I want to visit is: Bengaluru
```

The bot will return a customized 3-day itinerary based on the PDF content.

## 🛠️ Tech Stack

* **SentenceTransformers**: For semantic embeddings (all-MiniLM-L6-v2)
* **FAISS**: Vector similarity search
* **PyMuPDF (fitz)**: For PDF parsing
* **LangChain + Ollama**: For prompt management and Mistral LLM-based responses
* **Mistral via Ollama**: Local LLM for fast, private generation

## 📌 Notes

* Ensure you have Ollama installed and running locally
* Replace `tour-guide.pdf` with your own travel content to customize destinations

## 👩‍💻 Author

Fatima Amani  
GitHub: [@fatima-amani](https://github.com/fatima-amani)
