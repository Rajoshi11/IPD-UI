import streamlit as st
import pandas as pd
import os

# Define the Streamlit app
def main():
    # Add a file upload widget to the app
    uploaded_file = st.file_uploader("Choose a file")

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
        st.write(df)

# Run the Streamlit app
if __name__ == "__main__":
    main()
