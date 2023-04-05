import streamlit as st 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
import streamlit as st
import pandas as pd
import os

def load_view():
    # Define the Streamlit app
        # Add a file upload widget to the app
    st.subheader('1. Dataset')
    
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            padding-top: 50px !important;
        }
        section[data-testid="stSidebar"][aria-expanded="false"]{
            padding-top: 50px !important;
        }
        .css-1rs6os{
        padding-top: 50px !important;
        }
        .css-10zg0a4{
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
        st.header("Uploaded Dataset")
        st.markdown('**1.1. Glimpse of dataset**')
        st.write(df)
        le = LabelEncoder()
        df['Presence'] = le.fit_transform(df['Presence'])
        df['Well Name'] = le.fit_transform(df['Well Name'])
        df['Formation'] = le.fit_transform(df['Formation'])
        # Display the preprocessed data
        st.header("Encoded Feature Variables: Geological and Physical factors")
        X = df.iloc[:,:-1]
        st.write(X)
        st.header("Encoded Target Variable: Presence of oil and gas")
        Y = df.iloc[:,-1]
        st.write(Y)



        # Step 3: Model Training
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, max_depth=5)
        model.fit(X_train, Y_train)



        # Step 4: Model Deployment
        with open("trained_model.pkl", "wb") as f:
            pickle.dump(model, f)
        
        def download_pickle_file():
            with open("trained_model.pkl", "rb") as f:
                pickle_file = f.read()
            return pickle_file

        if st.button("Click Here to download the trained model"):
            pickle_file = download_pickle_file()
            st.download_button(label="Download Trained Model",
                            data=pickle_file,
                            file_name="trained_model.pkl",
                            mime="application/octet-stream")

    



















