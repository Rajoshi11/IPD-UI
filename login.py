import streamlit as st 
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# Authentication
names = ["Peter Parker"]
usernames = ["fc-solutions"]

# Load Hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                }          
            }
        }


authenticator = stauth.Authenticate(credentials,"sales_dashboard","abcdef",cookie_expiry_days=0)
name,authentication_status,username = authenticator.login("Fuel Cycle","main")
if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    st.write("hello")