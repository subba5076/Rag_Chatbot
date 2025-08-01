# document_loader.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_chunk_docs(doc_paths):
    all_docs = []
    for path in doc_paths:
        ext = os.path.splitext(path)[-1].lower()
        if ext == ".pdf":
            loader = PyPDFLoader(path)
            docs = loader.load()
        elif ext == ".txt":
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            docs = [Document(page_content=text)]
        else:
            continue
        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(all_docs)
