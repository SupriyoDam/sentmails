import streamlit as st
from src.loadserver import LoadServer
from src.emailsender import EmailSender
import os
from PIL import Image


PWD = os.path.dirname(os.path.abspath(__file__))
st.title("Email Service Clone")

left_side, right_side = st.columns([2, 1])

with left_side:
    path = os.path.join(PWD, 'static', 'pictures', 'email_background.png')
    image = Image.open(path)
    st.image(image)

with right_side:
    st.subheader("Login Page")

    # st.write('Email')
    id = st.text_input("Email ID")
    pw = st.text_input('Password')
    st.button('Login')

    if id=="admin" and pw == "root":
        validation = True

    else:
        validation = False
    
    if validation:
        st.subheader('Login Successfull.')
