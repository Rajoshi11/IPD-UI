import streamlit as st
import utils as utl
from views import EDA, home, AutoMlRegressionApp, AutoMlClassificationApp, TheMachineLearningHyperparameterOptimizationApp, training , prediction
import json
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time

st.set_page_config(layout="wide", page_title='Oil and Gas Exploration')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_success = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_dj2iGEFiUX.json")
col1, col2, col3 = st.columns((1, 7, 1))
with col2:
    with st_lottie_spinner(lottie_success, loop=False, key="progress"):
        time.sleep(3)

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

#page_bg_img = f"""
#    <style>
 #      [data-testid="stAppViewContainer"] > .main {{
  #        background-image: url("https://wallpaperaccess.com/full/2941149.jpg");
   #      background-size: cover; }}
    # [data-testid = "stcss-6qob1r] > .main {{
     #   background-image: url("https://wallpaperaccess.com/full/2941149.jpg");
    #   background-size: cover;
  #}}    
#"""
#st.markdown(page_bg_img, unsafe_allow_html=True)'''

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "EDA":
        EDA.load_view()
    elif route == "AutoMlRegressionApp":
        AutoMlRegressionApp.load_view()
    elif route == "AutoMlClassificationApp":
        AutoMlClassificationApp.load_view()
    elif route == "TheMachineLearningHyperparameterOptimizationApp":
        TheMachineLearningHyperparameterOptimizationApp.load_view()
    elif route == "Training":
        training.load_view()
    elif route == "Prediction":
        prediction.load_view() 
    elif route == None:
       home.load_view()


        
navigation()