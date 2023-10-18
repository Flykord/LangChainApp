# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from llama_index import download_loader
from llama_index.readers.schema import Document

file_path = "C:/Users/vazquezd/Desktop/GPT ak.txt"

with open(file_path) as f:
    lines = f.readlines()
    

openai.api_key = lines[0]
st.header("Chat with the Streamlit docs 💬 📚")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
    ]
    
    
#Add data from llama hub
from llama_index import download_loader

ArxivReader = download_loader("ArxivReader")

loader = ArxivReader()
documents = loader.load_data(search_query='cat:all')




chat_engine = documents.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history