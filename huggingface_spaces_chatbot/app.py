from langchain import OpenAI

import os
#from constants import openai_key
import streamlit as st
from dotenv import load_dotenv




#Load environment variable

load_dotenv()  #take environment variable from .env

#os.environ["OPENAI_API_KEY"]=openai_key

#function to load Open AI model and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response=llm(question)
    return response

#INITIALISE OUR STREAMLIT APP

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ", key="input")

response = get_openai_response(input)

submit=st.button("Ask the question")

#IF SUBMIT BUTTON Is clicked

if submit:
    st.subheader("The response is ")
    st.write(response)







