# 🧠 LLM-Powered Chatbot with RAG on Custom Domain (Local Inference)
<img width="829" height="483" alt="image" src="https://github.com/user-attachments/assets/0e4cf32d-d05b-4ae3-bb85-d38430c11329" />

A fully local Retrieval-Augmented Generation (RAG) chatbot built using LangChain and Hugging Face Transformers. It supports question-answering over custom documents without relying on any external API — everything runs locally.

---

## ✅ Features

- Upload `.pdf` and `.txt` files as knowledge base
- Chunk and embed documents using `sentence-transformers`
- Perform semantic search with FAISS
- Answer questions using a local LLM (`flan-t5-base`)
- Interactive web interface built with Streamlit

---

## 🗂️ Project Structure

```bash
rag_chatbot/
├── app.py                  # Main Streamlit app
├── document_loader.py      # Loads and chunks documents
├── vector_store.py         # Handles FAISS vector store
├── qa_chain.py             # Builds the RetrievalQA chain using local LLM
├── docs/                   # Folder for uploaded documents
├── .env                    # For future API support (optional)
├── requirements.txt        # Python dependencies
└── assets/
    └── working_demo.png    # Screenshot of the app in action




