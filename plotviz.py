import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import openai
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv
import time

st.set_page_config(page_title="Chat with Your Book", page_icon="📚", layout="wide")
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
llm_openai = OpenAI(model="gpt-3.5-turbo")
embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

file_uploader = st.file_uploader("Upload a text file", type=["txt", "epub"])

if file_uploader:
    with st.spinner("Processing file..."):
        if not os.path.exists('./data'):
            os.mkdir('./data')
        file_path = os.path.join('./data', file_uploader.name)
        with open(file_path, "wb") as f:
            f.write(file_uploader.getbuffer())  # save the uploaded file
        documents = SimpleDirectoryReader('./data').load_data()
        index = VectorStoreIndex.from_documents(documents, embed_model=embedding_model)
        index.
        query_engine = index.as_query_engine(llm=llm_openai)

    question = st.text_area("Enter your query")
    if st.button("Ask"):
        if question:
            with st.spinner("Retrieving and summarizing answer..."):
                #time.sleep(2)
                response = query_engine.query(question)
                st.success(response)
