#integrate our code with openAI API

import os
from constants import openai_key
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#streamlit framework

st.title('Langchain Demo WITH Open AI API')

#create text box to write input for chat

input_text=st.text_input('search the topic you want to search')

#OPEN AI LLM models

#temperature mentions how much control agent should have while providing you the response
#VALUE OF temperature is between 0 to 1

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))



