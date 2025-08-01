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
```
# Step 1: Clone the repository
git clone https://github.com/yourusername/rag_chatbot.git
cd rag_chatbot

# Step 2: Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Step 3: Install dependencies

pip install streamlit langchain faiss-cpu sentence-transformers transformers pypdf python-dotenv

# Step 4: Run the Streamlit app
streamlit run app.py


##🔧 Built With
LangChain

Sentence Transformers

Hugging Face Transformers

FAISS

Streamlit

## 📄 License
MIT License – feel free to use, modify, and share.




