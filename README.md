# 🧠 LLM-Powered Chatbot with RAG on Custom Domain (Local Inference)
<img width="829" height="483" alt="image" src="https://github.com/user-attachments/assets/0e4cf32d-d05b-4ae3-bb85-d38430c11329" />


This project is a fully local Retrieval-Augmented Generation (RAG) chatbot that answers questions over your own documents using a local LLM (`flan-t5-base`). It uses FAISS for semantic search and Streamlit for an interactive frontend.

---

## ✅ Features

- 🔍 Upload and query your own documents (`.pdf` or `.txt`)
- 🧠 Local embedding using `sentence-transformers`
- ⚡ Fast similarity search with FAISS
- 🤖 Answer generation with a local Hugging Face model (`transformers.pipeline`)
- 💻 Streamlit-based user interface
- 🔌 No OpenAI or Hugging Face APIs required

---

## 🗂️ Project Structure
rag_chatbot/
├── app.py # Main Streamlit app
├── document_loader.py # Loads and chunks documents
├── vector_store.py # Handles FAISS vector store
├── qa_chain.py # Builds the RetrievalQA chain using local LLM
├── docs/ # Folder for uploaded documents
├── .env # For future API support (optional)
├── requirements.txt # Python dependencies
└── assets/
└── working_demo.png # Screenshot of the app in action



