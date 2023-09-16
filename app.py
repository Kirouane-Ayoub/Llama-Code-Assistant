import streamlit as st
from PIL import Image
from lib.utils import *
img = Image.open("icon.png")

st.set_page_config(page_title='Llama Code Assistant',page_icon = img)
st.sidebar.image("icon.png" , width=250)
st.header(":hand: Welcome To Llama Code Assistant : ")
st.info("""
"Llama Code Assistant," is a powerful tool built upon a massive 34 billion-parameter
generative text model. This model, available in the Hugging Face Transformers format, 
is designed for various code-related tasks, including code synthesis and comprehension. 
It serves as a valuable resource for developers and programmers by assisting them in writing,
understanding, and generating code.""")
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi :hand: Im your Code Assistant,Enter Your code related Instruction."}]
# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)    