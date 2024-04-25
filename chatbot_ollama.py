from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#Langsmith tracking
#os.environ['LANGCHAIN_TRACING_V2']="true"
#os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

#prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant, please respond to the queries"),
        ("user","Question:{question}")


    ]
)

#streamlit framework

st.title("Open AI Demo")
input_text=st.text_input("search the topic")

#OPEN AI LLM

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))