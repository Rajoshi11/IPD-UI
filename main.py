import streamlit as st
import utils as utl
from views import EDA, home, AutoMlRegressionApp, AutoMlClassificationApp, TheMachineLearningHyperparameterOptimizationApp, options,configuration

st.set_page_config(layout="wide", page_title='Oil and Gas Exploration')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

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
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()