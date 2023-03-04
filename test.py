import streamlit as st
import pandas as pd
import os
import featuretools as ft
from sklearn.preprocessing import MinMaxScaler
# Define the Streamlit app
def main():
    # Add a file upload widget to the app
    uploaded_file = st.file_uploader("Choose a file")

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


        # Define the preprocessing steps
        options = {
            "Data cleaning": clean_data,
            "Data transformation": transform_data,
            "Feature engineering": engineer_features,
            "Data normalization": normalize_data
        }

        # Add a widget to allow the user to select the preprocessing steps
        selected_options = st.multiselect("Select preprocessing options", list(options.keys()))

        # Apply the selected preprocessing steps to the data
        for option in selected_options:
            df = options[option](df)

# Define the data cleaning function
def clean_data(df):
    # Load the CSV file into a Pandas DataFrame
    # df = pd.read_csv("data.csv")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert data types
    df['Date'] = pd.to_datetime(df['Date'])
    df['Value'] = pd.to_numeric(df['Value'])

    # Remove outliers
    df = df[df['Value'] > 0]

    # Save the cleaned data to a new CSV file
    df.to_csv("cleaned_data.csv", index=False)

    return df

# Define the data transformation function
def transform_data(df):
    # Load the CSV file into a Pandas DataFrame
    # df = pd.read_csv("data.csv")

    # Transform the data
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df['Value'] = df['Value'].apply(lambda x: x * 1000)
    df['Category'] = df['Category'].astype('category')

    # Save the transformed data to a new CSV file
    df.to_csv("transformed_data.csv", index=False)

    return df

# Define the feature engineering function
def engineer_features(df):

    # Load the CSV file into a Pandas DataFrame
    # df = pd.read_csv("data.csv")

    # Create an entityset and add the data to it
    es = ft.EntitySet(id='data')
    es.entity_from_dataframe(entity_id='data', dataframe=df, index='id')

    # Define the time index
    es['data']['Date'] = pd.to_datetime(es['data']['Date'])

    # Define the relationships between entities
    relationships = []

    # Create the feature matrix
    fm, features = ft.dfs(entityset=es, target_entity='data', agg_primitives=['mean', 'max', 'min'], trans_primitives=['diff', 'time_since_previous'])

    # Save the feature matrix to a new CSV file
    fm.to_csv("features.csv", index=False)

    return df

# Define the data normalization function
def normalize_data(df):

    # Load the CSV file into a Pandas DataFrame
    # df = pd.read_csv("data.csv")

    # Select the columns to normalize
    columns_to_normalize = ['column1', 'column2', 'column3']

    # Perform the data normalization
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    # Save the normalized data to a new CSV file
    df.to_csv("normalized_data.csv", index=False)

    return df

# Run the Streamlit app
if __name__ == "__main__":
    main()
