import streamlit as st

def load_view():
    #st.markdown("<span style = 'color:#0c243c; font-family:sans-serif; font-size:35px;'>Predictive Analysis of Oil and Gas using Well Log Data</span>",unsafe_allow_html=True)
    '''page_bg_img = f"""
        <style>
            [data-testid="stAppViewContainer"] > .main {{
                background-image: url("https://wallpaperaccess.com/full/2941149.jpg");  
                background-size:cover}}"""
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # Define the page title and favicon
    #st.set_page_config(page_title="Oil and Gas Exploration", page_icon=":oil_drum:")'''

    # Set up the layout
    st.markdown("<span style = 'font-family:sans-serif; font-size:35px;'>Predictive Analysis of Oil and Gas using Well Log Data</span>",unsafe_allow_html=True)
    #st.title("Oil and Gas Exploration Project")
    st.markdown("---")
    title = f"""
            <div class = "header">Project Overview</div>"""
    st.markdown(title,unsafe_allow_html=True)

    # Display project overview
    #st.header("Project Overview")
    title1 = f"""
    <div class = "header1">Welcome to our Predictive analysis of oil and gas exploration project! Our team is dedicated to analyse presence oil and gas in well logs and improving our understanding of the geology and natural resources of area. Here are some quick facts about our project:
    </div>"""
    st.markdown(title1,unsafe_allow_html=True)
    #st.write("Welcome to our Predictive analysis of oil and gas exploration project! Our team is dedicated to analyse presence oil and gas in well logs and improving our understanding of the geology and natural resources of area. Here are some quick facts about our project:")

    # Display project information in cards
    col1, col2, col3 = st.columns(3)

    with col1:
        #title2 = f"""
        #    <div class = "header2">**Well logs:** 10</div>"""
        #st.markdown(title2,unsafe_allow_html=True)
        st.info("**Well logs:** 10")
        
    with col2:
        #title3 = f"""
        #    <div class = "header3">**Geological and Physical Factors:** 11</div>"""
        #st.markdown(title3,unsafe_allow_html=True)
        st.success("**Geological and Physical Factors:** 11")
        
    with col3:
        #title4 = f"""
        #    <div class = "header4">**Facies:** 9</div>"""
        #st.markdown(title4,unsafe_allow_html=True)
        st.warning("**Facies:** 9")
        
    # Display project bulletin
    title5 = f"""
            <div class = "header5">Project Bulletin</div>"""
    st.markdown(title5,unsafe_allow_html=True)
    #st.header("Project Bulletin")
    title6 = f"""
            <div class = "header6">Stay up-to-date on the latest news and developments from our project. Check out our latest bulletin below:</div>"""
    st.markdown(title6,unsafe_allow_html=True)
    #st.write("Stay up-to-date on the latest news and developments from our project. Check out our latest bulletin below:")

    Bulletin_image = 'Bulletin2.png'
    st.image(Bulletin_image, use_column_width=False)
    ocean_writeup = f"""<div class = "header6>
    Well log data is a type of subsurface exploration data that provides information on the geological and physical properties of the rocks and fluids within a wellbore. The variation of these properties can be observed through different types of well log data, which include:

    Gamma ray logs: These logs measure the natural radiation emitted by rocks, which is related to their mineralogy and lithology. 

    Resistivity logs: These logs measure the electrical resistivity of the rocks, which is related to their porosity and fluid content.

    Sonic logs: These logs measure the travel time of sound waves through the rocks, which is related to their density and elastic properties.

    Density logs: These logs measure the bulk density of the rocks, which is related to their mineralogy and porosity.

    Overall, the variation of geological and physical features of well log data can provide important information for the interpretation of subsurface geological structures and fluid content, which is crucial for exploration and production of natural resources such as oil and gas.</div>
    """
    st.markdown(ocean_writeup,unsafe_allow_html=True)




    # Display images of the exploration site
    title7 = f"""
            <div class = "header7">Exploration Site Images</div>"""
    st.markdown(title7,unsafe_allow_html=True)
    #st.header("Exploration Site Images")

    title8 = f"""
            <div class = "header8">Take a look at some images of exploration sites:</div>"""
    st.markdown(title8,unsafe_allow_html=True)
    #st.write("Take a look at some images of exploration sites:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("image1.jpg", use_column_width=True)

    with col2:
        st.image("image2.jpeg", use_column_width=True)

    with col3:
        st.image("image3.jpeg", use_column_width=True)

    # Display videos of the exploration site
    title9 = f"""
            <div class = "header9">Exploration Site Videos</div>"""
    st.markdown(title9,unsafe_allow_html=True)
    #st.header("Exploration Site Videos")
    title10 = f"""
            <div class = "header10">Check out some videos of exploration site:</div>"""
    st.markdown(title10,unsafe_allow_html=True)
    #st.write("Check out some videos of exploration site:")

    col1, col2 = st.columns(2)

    with col1:
        st.video("video1.webm", start_time=10)

    with col2:
        st.video("video2.webm", start_time=30)

    # Display contact information
    title11 = f"""
            <div class = "header11">Contact Us</div>"""
    st.markdown(title11,unsafe_allow_html=True)
    #st.header("Contact Us")
    '''title12 = f"""
            <div class = "header12">If you have any questions or would like to learn more about our project, please contact us:</div>
            <div class = "header12"- Email: info@oilgasexploration.com</div>
            <div class = "header12"- Phone: 1-800-OIL-GAS>/div>
            <div class = "header12"- Address: 123 Main Street, Houston, TX 77002</div>
    st.markdown(title12,unsafe_allow_html=True)'''
    title12 = f"""
            <div class = "header12">If you have any questions or would like to learn more about our project, please contact us:</div>"""
    st.markdown(title12,unsafe_allow_html=True)
    #st.write("If you have any questions or would like to learn more about our project, please contact us:")
    title13 = f"""
            <div class = "header12">- Email: info@oilgasexploration.com</div>"""
    st.markdown(title13,unsafe_allow_html=True)
    #st.write("- Email: info@oilgasexploration.com")
    title14 = f"""
            <div class = "header12">- Phone: 1-800-OIL-GAS</div>"""
    st.markdown(title14,unsafe_allow_html=True)
    #st.write("- Phone: 1-800-OIL-GAS")
    title15 = f"""
            <div class = "header12">- Address: 123 Main Street, Houston, TX 77002</div>"""
    st.markdown(title15,unsafe_allow_html=True)
    #st.write("- Address: 123 Main Street, Houston, TX 77002")




































'''import os 
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
    #image1 = <div style = "background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")">
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
      name = <div style = "background-color: #DEF2F1; outline-style: solid;outline-color: #3AAFA9; padding: 20px; padding-bottom:40px;border-radius:30px">
                <h1 style ="color: #0c243c">Abstract</h1>
                <p style ='color:#3AAFA9'>Predictive  analysis providies valuable insights into the geological characteristics of reservoir rocks, a process carried out by geoscientists in development and exploration operations. 
                But due to issues with data quality, complexity of the geology, subjectivity of interpretation, scarcity of data, and lack of standardisation, describing various facies accurately can be 
                challenging. In order to overcome these difficulties, cutting-edge methods can be utilised to increase the precision and consistency of oil prediction results, including the integration of 
                various types of data from rock samples and machine learning algorithms.</p>
      st.markdown(name, unsafe_allow_html=True)
    st.markdown("#")
    #with col3:
    #    with st.container():
    #    #image = <div style = "outline-style:solid; outline-color: #3AAFA9"</div>
    #    # bnst.markdown(image,unsafe_allow_html=True)
    #        st.markdown(
    #        <style>
    #        div [data_test_id = "stimage"]{
    #        border : 1px solid #3AAFA9
    #        }
    #        </style>
    #        ,unsafe_allow_html=True)
    #        image = Image.open('assets/images/oil and gas.jpg')
    #        st.image(image, width=500,caption="Oil and Gas using Well Log")

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

    col1, col2 = st.columns((2,3))
    with col1:
        st.image("https://j.gifs.com/vMXj4O.gif", width=500, caption="Representation of Oil Extraction from Rig Wells")
    with col2:
        original_title = <div style="background-color: grey; padding: 20px;padding-bottom: 40px; border-radius: 30px">
                            <h2>Abstract</h2>
                            <p style="font-size: 25px;"> • Facies classification is one of the most important tasks that geoscientists work on development and exploration projects.</p>
                            <p style="font-size: 25px;"> • New Ways of cutting operations cost , enhancing efficiency and increasing out-turn for oil and gas companies to identify the region in which they must drill where chances of extraction of oil are much higher.</p>
                            </div>
                            
        st.markdown(original_title, unsafe_allow_html=True)

    st.markdown("#")
    
    col1, col2, col3 = st.columns((2,3,1))
    with col2:
        st.header("System Architecture and Diagram" )
    image = Image.open('assets/images/systemarch.png')
    st.image(image, caption='System architecture and Block Diagram  ', width=1400)'''




    
    