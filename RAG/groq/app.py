import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import time

from dotenv import load_dotenv

load_dotenv()

#load the GROQ and Open AI API key

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

groq_api_key=os.environ['GROQ_API_KEY']


st.title("CHATGROQ with LLama3 Demo")

llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="Llama3-8b-8192")


prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)


prompt1=st.text_input("Enter your question from documents")

def vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.loader=PyPDFDirectoryLoader("./us_census") #document ingestion
        st.session_state.docs=st.session_state.loader.load()#document loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) #chunk creation
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])#splitting
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)





if st.button("Documents Embedding"):
    vector_embeddings()
    st.write("vector store DB is ready")



if prompt1:
    start=time.process_time()

    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retriever_chain=create_retrieval_chain(retriever,document_chain)

    
    response = retriever_chain.invoke({'input':prompt1})

    print("Response time :",time.process_time()-start)

    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")






