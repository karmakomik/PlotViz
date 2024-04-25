import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
#rom langchain.vectorstores import Vectara
from langchain_community.llms import OpenAI
from llama_index.core import SimpleDirectoryReader
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#VECTARA_CUSTOMER_ID = os.getenv("VECTARA_CUSTOMER_ID")
#VECTARA_API_KEY = os.getenv("VECTARA_API_KEY")
#VECTARA_CORPUS_KEY = os.getenv("VECTARA_CORPUS_ID")



'''
def langchain_func(file, question):
    loader = TextLoader(file, encoding= 'utf8')
    documents = loader.load()
    vectara = Vectara.from_documents(documents, embedding=None)
    qa = RetrievalQA.from_llm(llm=OpenAI(), retriever = vectara.as_retriever())
    answer = qa({'query': question})
    return answer
'''

st.set_page_config(page_title="PlotViz", page_icon="📚", layout="wide")
file_uploader = st.file_uploader("Upload a text file", type=["txt", "epub"])

if file_uploader is not None:
    if not os.path.exists('./data'):
        os.mkdir('./data')
        
    file_name = file_uploader.name
    with open(os.path.join(file_name), "wb") as f: 
        f.write(file_uploader.getbuffer()) # write the file to the uploaded folder

    question = st.text_area("Enter your query")
    if st.button("Ask"):
        if len(question) > 0:
            answer = langchain_func(file_name, question)
            st.info("Your query: " + question)
            st.success(answer)
