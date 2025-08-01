import streamlit as st
from document_loader import load_and_chunk_docs
from vector_store import create_vectorstore, load_vectorstore
from qa_chain import load_qa_chain

st.title("📚 Domain-Specific Chatbot (RAG)")

uploaded_files = st.file_uploader("Upload your documents", accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Loading and indexing..."):
        doc_paths = []
        for f in uploaded_files:
            path = f"docs/{f.name}"
            with open(path, "wb") as f_out:
                f_out.write(f.read())
            doc_paths.append(path)

        chunks = load_and_chunk_docs(doc_paths)
        vectordb = create_vectorstore(chunks)
        qa = load_qa_chain(vectordb)
        st.success("Documents indexed!")

    query = st.text_input("Ask a question about your documents:")
    if query:
        response = qa.invoke({"query": query})
        st.markdown(f"**Answer:** {response['result']}")

