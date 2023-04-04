import os 
# The OS module in Python provides functions for interacting with the operating system. 
import streamlit as st
import streamlit.components.v1 as com
# EDA packages : Exploitary data analysis
import pandas as pd
# Viz packages : Visualization packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # To help us to prevent erros while trying to plot
# The canonical renderer for user interfaces is Agg which uses the Anti-Grain Geometry C++ library to make a raster (pixel) image of the figure.
# Like in tiknter it is matplotlib.use('TkAgg')
import seaborn as sns
import base64
from PIL import Image

def load_view():
    #image1 = '''<div style = "background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")">'''
    #st.markdown(image1,unsafe_allow_html=True)
    st.markdown("<span style = 'color:#0c243c; font-family:sans-serif; font-size:35px;'>Predictive Analysis of Oil and Gas using Well Log Data</span>",unsafe_allow_html=True)
    page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://wallpaperaccess.com/full/2941149.jpg");  
            background-size:cover}}"""
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    col1,col2,col3= st.columns((7,7,5))
    with col1:
      name = '''<div style = "background-color: #DEF2F1; outline-style: solid;outline-color: #3AAFA9; padding: 20px; padding-bottom:40px;border-radius:30px">
                <h1 style ="color: #0c243c">Abstract</h1>
                <p style ='color:#3AAFA9'>Predictive  analysis providies valuable insights into the geological characteristics of reservoir rocks, a process carried out by geoscientists in development and exploration operations. 
                But due to issues with data quality, complexity of the geology, subjectivity of interpretation, scarcity of data, and lack of standardisation, describing various facies accurately can be 
                challenging. In order to overcome these difficulties, cutting-edge methods can be utilised to increase the precision and consistency of oil prediction results, including the integration of 
                various types of data from rock samples and machine learning algorithms.</p>'''
      st.markdown(name, unsafe_allow_html=True)
    st.markdown("#")
    #with col3:
    #    with st.container():
    #    #image = '''<div style = "outline-style:solid; outline-color: #3AAFA9"</div>'''
    #    # bnst.markdown(image,unsafe_allow_html=True)
    #        st.markdown('''
    #        <style>
    #        div [data_test_id = "stimage"]{
    #        border : 1px solid #3AAFA9
    #        }
    #        </style>
    #        ''',unsafe_allow_html=True)
    #        image = Image.open('assets/images/oil and gas.jpg')
    #        st.image(image, width=500,caption="Oil and Gas using Well Log")'''

    #<img src="oil and gas.jpg" height ="300" width="300" alt="oilandgas image"/>
    #st.set_option('deprecation.showPyplotGlobalUse', False)

    # page_bg_img = f"""
    # <style>
    # [data-testid="stAppViewContainer"] > .main {{
    # background-image: url("https://unsplash.com/photos/XLFu0PM5Qsg");
    # }}
    # """
    # st.markdown(page_bg_img, unsafe_allow_html=True)
    #col1, col2, col3 = st.columns((2,7,1))
    #with col2:
    #    st.subheader("Problem definition:" )
    #st.markdown("#")
    #st.markdown("""
    #<style>
    #  section[data-testid="stSidebar"][aria-expanded="true"]{
    #    padding-top: 50px !important;
    #  }
    #  section[data-testid="stSidebar"][aria-expanded="false"]{
    #    padding-top: 50px !important;
    #  }
    #</sstyle>""", unsafe_allow_html=True)

    """col1, col2 = st.columns((2,3))
    with col1:
        st.image("https://j.gifs.com/vMXj4O.gif", width=500, caption="Representation of Oil Extraction from Rig Wells")
    with col2:
        original_title = '''<div style="background-color: grey; padding: 20px;padding-bottom: 40px; border-radius: 30px">
                            <h2>Abstract</h2>
                            <p style="font-size: 25px;"> • Facies classification is one of the most important tasks that geoscientists work on development and exploration projects.</p>
                            <p style="font-size: 25px;"> • New Ways of cutting operations cost , enhancing efficiency and increasing out-turn for oil and gas companies to identify the region in which they must drill where chances of extraction of oil are much higher.</p>
                            </div>
                            '''
        st.markdown(original_title, unsafe_allow_html=True)

    st.markdown("#")
    
    col1, col2, col3 = st.columns((2,3,1))
    with col2:
        st.header("System Architecture and Diagram" )
    image = Image.open('assets/images/systemarch.png')
    st.image(image, caption='System architecture and Block Diagram  ', width=1400)"""




    
    