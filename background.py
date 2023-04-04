import base64
import streamlit as st 
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.1);
        color: #000000;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# data:image/{"png"}
add_bg_from_local('Background.png')
st.header("hello")   