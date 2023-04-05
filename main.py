import streamlit as st
import utils as utl
from views import EDA, home, AutoMlRegressionApp, AutoMlClassificationApp, TheMachineLearningHyperparameterOptimizationApp, training , prediction


st.set_page_config(layout="wide", page_title='Oil and Gas Exploration')
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
<<<<<<< HEAD
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
       home.load_view()
=======
    elif route == "Training":
        training.load_view()
    elif route == "Prediction":
        prediction.load_view() 
    elif route == None:
       home.load_view()


>>>>>>> 0b22d8ca9be0a434507f961cd3c6f54191ee67f1
        
navigation()