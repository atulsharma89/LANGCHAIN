#integrate our code with openAI API

import os
from constants import openai_key
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
import streamlit as st

#for custom searches we can use prompt engineering

from langchain import PromptTemplate
from langchain.chains import LLMChain  #responsible for executing prompt  templates
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain


os.environ["OPENAI_API_KEY"]=openai_key

#streamlit framework

st.title('Langchain Demo WITH Open AI API')

#create text box to write input for chat

input_text=st.text_input('Celabrity search results')


#prompt template

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celabrity{name} "
)



#OPEN AI LLM models

#temperature mentions how much control agent should have while providing you the response
#VALUE OF temperature is between 0 to 1

llm=OpenAI(temperature=0.8)
chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person')


second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="when was {person} born "
)

chain2 = LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')


third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events around {dob} inthe world  "
)

chain3 = LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='description')

#parent_chain=SimpleSequentialChain(chains=[chain,chain2],verbose=True)



parent_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variables= ['person','dob','description'],verbose=True)


if input_text:
    #st.write(parent_chain.run(input_text))
    st.write(parent_chain({'name': input_text}))



