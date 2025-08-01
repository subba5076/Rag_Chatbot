from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

def create_vectorstore(chunks, persist_path="vectorstore"):
    embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vectordb = FAISS.from_documents(chunks, embedding_model)
    vectordb.save_local(persist_path)
    return vectordb

def load_vectorstore(persist_path="vectorstore"):
    embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    return FAISS.load_local(persist_path, embedding_model)
