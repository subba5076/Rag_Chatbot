from transformers import pipeline
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

def load_qa_chain(vectorstore):
    local_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",   # or mistralai/Mistral-7B-v0.1 if GPU
        max_new_tokens=256,
        temperature=0.5
    )

    llm = HuggingFacePipeline(pipeline=local_pipeline)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa_chain
