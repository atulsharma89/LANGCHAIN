#conversation AI


import langchain
import os
from constants import openai_key
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#streamlit UI

st.set_page_config(page_title="Conversation QA Chatbot")
st.header("Hey Let's chat")

#Load environment variable


os.environ["OPENAI_API_KEY"]=openai_key

#from dotenv import load_dotenv
#load_dotenv()

#
chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[SystemMessage(content='you are a comdeian AI assistant ')]

def get_openai_response(question):
    #llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    #setting up session state
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    #once we got the asnwer we need to append this to AI message
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    #response=llm(question)
    return answer.content

#when we give question that becomes huma message
#defualt domain message: like "you need to act like a comedian" --> system message
#whenever LLM model provides reponse: AI message

#WE NEED to store these in sessions so that chatbot can remeber the context

input=st.text_input("Input: ", key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

#IF THE ASK BUTTON IS CLICKED

if submit:
    st.subheader("The response is ")
    st.write(response)

