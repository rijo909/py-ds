import sys
import streamlit as st
import numpy as np
from PIL import Image
import google.generativeai as genai


sys.path.append(r'C:\Users\rijok\Documents')

from colab_api import api_key

# Use the key
print(api_key)

if 'model' not in st.session_state:
    genai.configure(api_key=api_key)
    st.session_state['model']=genai.GenerativeModel('models/gemini-1.5-flash')
    st.session_state['chatbot']=st.session_state['model'].start_chat(history=[])
    st.session_state['history']=[]
st.title('Flash Bot light⚡🤖')
# UI
col1, col2 = st.columns([7, 1])
with col1:
    user_text = st.text_input('type your chat here...')
    file=st.file_uploader('upload Image', type=['jpg', 'jpeg', 'png'])
    send=st.button('Send')
    clear=st.button('Clear History')
    view_history=st.button('View History')

# code
if user_text and file and send:
    img=Image.open(file)
    chatbot=st.session_state['chatbot']
    res=chatbot.send_message([img, user_text]).text
    st.session_state['history'].append((user_text, res))
    st.write(f'Bot🤖 : {res}')
elif user_text and send:
    chatbot=st.session_state['chatbot']
    res=chatbot.send_message([user_text]).text
    st.session_state['history'].append((user_text, res))
    st.write(f'Bot🤖 : {res}')
elif not user_text and send:
    st.warning('No text entered!')

if clear and st.session_state['history']:
    st.session_state['chatbot']=st.session_state['model'].start_chat(history=[])
    st.session_state['history'].clear()
    st.success('History Cleared')
elif clear and not st.session_state['history']:
    st.warning('No History to clear')


if view_history and st.session_state['history']:
    for i,j in st.session_state['history']:
        st.write(f'**User👦 :** {i}')
        st.write(f'**Bot🤖 :** {j} \n')
        st.write('\n')

    st.write(f'❌ -- end of  conversation -- ❌')
    
elif view_history and not st.session_state['history']:
    st.warning('No History')
