import streamlit as st
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

def load_view():
    st.header('1. Dataset')
    # Define the Streamlit app
    # Add a file upload widget to the app
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            padding-top: 50px !important;
        }
        section[data-testid="stSidebar"][aria-expanded="false"]{
            padding-top: 50px !important;
        }
        .css-10zg0a4{
            padding-top: 50px !important;
        }
        .css-1rs6os{
        padding-top: 50px !important;
        }
    </style>""", unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader("Choose a file")

    # If the user uploads a file
    if uploaded_file is not None:
        # Get the name and extension of the uploaded file
        filename = uploaded_file.name
        extension = os.path.splitext(filename)[1]

        # If the file is a CSV file
        if extension == ".csv":
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(uploaded_file)

        # If the file is an Excel file
        elif extension in [".xls", ".xlsx"]:
            # Read the Excel file into a Pandas DataFrame
            df = pd.read_excel(uploaded_file)

            # Convert the Excel file to a CSV file
            csv_filename = os.path.splitext(filename)[0] + ".csv"
            df.to_csv(csv_filename, index=False)
                
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(csv_filename)

        # If the file is a text file
        elif extension == ".txt":
            # Read the text file into a Pandas DataFrame
            df = pd.read_csv(uploaded_file, delimiter="\t")

            # Convert the text file to a CSV file
            csv_filename = os.path.splitext(filename)[0] + ".csv"
            df.to_csv(csv_filename, index=False)

            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(csv_filename)

        # If the file is not in a supported format
        else:
            st.error("Unsupported file format")

        # Display the preprocessed data
        st.subheader("Uploaded Dataset")
        st.write(df)
        le = LabelEncoder()
        df['Well Name'] = le.fit_transform(df['Well Name'])
        df['Formation'] = le.fit_transform(df['Formation'])
        st.subheader("Upload the pickle file of trained model")
        model_file = st.file_uploader("Upload a trained model (pickle file)", type=["pkl"])
        if model_file is not None:
            model = pickle.load(model_file)
            predictions = model.predict(df)
            st.subheader("Predicted (encoded) target variable")
            st.write(predictions)
            # define the mapping between numbers and categories
            mapping = {0: "High", 1: "Low", 2: "Medium"}

            # create a Pandas Series from the numerical array
            series = pd.Series(predictions)

            # use the map() method to apply the mapping to the series
            categories = series.map(mapping)
            st.subheader("Predicted Presence of Oil and gas")
            # print the resulting categories
            st.write(categories)
        