import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 
st.set_option('deprecation.showPyplotGlobalUse', False)


def load_view():
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
    # Set up the layout
    st.title("Exploratory Data Analysis of Oil and Gas Presence")

    # Display information on the dataset
    st.header("Dataset")
    page2=f"""
           <div class="header13">Our dataset contains well log data from oil and gas exploration. It includes measurements such as Gamma Ray, Resistivity, and Porosity, as well as lithology and hydrocarbon presence labels. The goal is to use this data to identify areas with high potential for oil and gas presence.
           </div>"""
    st.markdown(page2,unsafe_allow_html=True)

    #st.write("Our dataset contains well log data from oil and gas exploration. It includes measurements such as Gamma Ray, Resistivity, and Porosity, as well as lithology and hydrocarbon presence labels. The goal is to use this data to identify areas with high potential for oil and gas presence.")

    # Display a bulletin on the importance of EDA
    st.header("Importance of Exploratory Data Analysis")
    page3=f"""
           <div class="header13">Exploratory Data Analysis (EDA) is a crucial step in any data science project. It involves examining and visualizing the data to gain insights and identify patterns. EDA helps to inform the choice of modeling techniques and can often uncover unexpected results.
           </div>"""
    st.markdown(page3,unsafe_allow_html=True)
    #st.info("Exploratory Data Analysis (EDA) is a crucial step in any data science project. It involves examining and visualizing the data to gain insights and identify patterns. EDA helps to inform the choice of modeling techniques and can often uncover unexpected results.")

    # Display an image of a well log
    st.header("Well Log Example")
    st.image("well_log.jpeg", use_column_width=False, caption="Example well log")

    # Display a video on the basics of well logging
    st.header("Video: Basics of Well Logging")
    # video_url = "https://www.youtube.com/watch?v=d98pziKypN8"
    st.video("basics.mp4", start_time=10)

    # Display information on the features of interest
    st.header("Features of Interest")
    page2=f"""
           <div class="header13">In our dataset, the following features are of particular interest for identifying areas with high potential for oil and gas presence:</div>"""
    st.markdown(page2,unsafe_allow_html=True)
    page4=f"""
           <div class="header13">- Gamma Ray</div>"""
    st.markdown(page4,unsafe_allow_html=True)
    page5=f"""
           <div class="header13">- Resistivity</div>"""
    st.markdown(page5,unsafe_allow_html=True)
    page6=f"""
           <div class="header13">- Porosity
           </div>"""
    st.markdown(page6,unsafe_allow_html=True)
    page7=f"""
           <div class="header13">- Density</div>"""
    st.markdown(page7,unsafe_allow_html=True)
    page8=f"""
           <div class="header13">- Photoelectric Effect</div>"""
    st.markdown(page8,unsafe_allow_html=True)
    page9=f"""
           <div class="header13">- Hydrocarbon Presence Labels</div>"""
    st.markdown(page9,unsafe_allow_html=True)
    #st.write("In our dataset, the following features are of particular interest for identifying areas with high potential for oil and gas presence:")
    #st.write("- Gamma Ray")
    #st.write("- Resistivity")
    #st.write("- Porosity")
    #st.write("- Density")
    #st.write("- Photoelectric Effect")
    #st.write("- Hydrocarbon Presence Labels")

    # Display a call-to-action for further analysis
    st.header("Next Steps")
    page10=f"""
           <div class="header13">Now that we've explored some of the basics of our dataset, let's dive deeper into the data and start building models to identify areas with high potential for oil and gas presence. Click the button below to start exploring!</div>"""
    st.markdown(page10,unsafe_allow_html=True)
    #st.write("Now that we've explored some of the basics of our dataset, let's dive deeper into the data and start building models to identify areas with high potential for oil and gas presence. Click the button below to start exploring!")
    page11=f"""
           <div class="header13">Let's get started!</div>"""
    st.markdown(page11,unsafe_allow_html=True)
    #st.write("Let's get started!")
    # Add a file upload widget to the app
    page12=f"""
           <div class="header13">Choose a file</div>"""
    st.markdown(page12,unsafe_allow_html=True)
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
            # Perform data analysis and visualization
            st.title("Predictive Analysis of Oil and Gas using Well Log Data")

            st.header("Data Overview")
            st.write("The well log data contains information about various properties of a well, including depth, gamma ray readings, porosity, permeability, resistivity, density and photoelectric effect.")

            st.write("Here is a sample of the data:")
            st.dataframe(df.head())

            st.write("The data has", len(df), "observations and", len(df.columns), "features.")

            st.header("Data Cleaning")
            st.write("We need to check for any missing values in the data.")
            if df.isnull().values.any():
                st.write("There are missing values in the data.")
                st.write(df.isnull().sum())
            else:
                st.write("There are no missing values in the data.")

            st.header("Exploratory Data Analysis")
            st.write("We will perform some exploratory data analysis to better understand the relationships between the features.")

            # Visualize distribution of gamma ray readings
            st.write("Distribution of Gamma Ray Readings")
            sns.displot(df, x="GR", bins=30)
            st.pyplot()

            # Visualize relationship between porosity and permeability
            st.write("Relationship between Resistivity and Photoelectric Effect")
            sns.scatterplot(data=df, x="ILD_log10", y="PE", hue="DeltaPHI", palette="coolwarm")
            st.pyplot()

            

            st.header("Conclusion")
            st.write("In this analysis, we explored the well log data and performed some initial data cleaning and exploratory data analysis. ")

            st.write("Further analysis could include more advanced feature engineering, model selection, and hyperparameter tuning to improve the accuracy of the predictive model.")






























# # Add a file upload widget to the app
# uploaded_file = st.file_uploader("Choose a file")

# # If the user uploads a file
# if uploaded_file is not None:
#     # Get the name and extension of the uploaded file
#     filename = uploaded_file.name
#     extension = os.path.splitext(filename)[1]

#     # If the file is a CSV file
#     if extension == ".csv":
#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(uploaded_file)

#     # If the file is an Excel file
#     elif extension in [".xls", ".xlsx"]:
#         # Read the Excel file into a Pandas DataFrame
#         df = pd.read_excel(uploaded_file)

#         # Convert the Excel file to a CSV file
#         csv_filename = os.path.splitext(filename)[0] + ".csv"
#         df.to_csv(csv_filename, index=False)
            
#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(csv_filename)

#     # If the file is a text file
#     elif extension == ".txt":
#         # Read the text file into a Pandas DataFrame
#         df = pd.read_csv(uploaded_file, delimiter="\t")

#         # Convert the text file to a CSV file
#         csv_filename = os.path.splitext(filename)[0] + ".csv"
#         df.to_csv(csv_filename, index=False)

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(csv_filename)

#     # If the file is not in a supported format
#     else:
#         st.error("Unsupported file format")

#     # Display the preprocessed data
#     st.write(df)
#     # Perform data analysis and visualization
#     st.title("Predictive Analysis of Oil and Gas using Well Log Data")

#     st.header("Data Overview")
#     st.write("The well log data contains information about various properties of a well, including depth, gamma ray readings, porosity, permeability, resistivity, density and photoelectric effect.")

#     st.write("Here is a sample of the data:")
#     st.dataframe(df.head())

#     st.write("The data has", len(df), "observations and", len(df.columns), "features.")

#     st.header("Data Cleaning")
#     st.write("We need to check for any missing values in the data.")
#     if df.isnull().values.any():
#         st.write("There are missing values in the data.")
#         st.write(df.isnull().sum())
#     else:
#         st.write("There are no missing values in the data.")

#     st.header("Exploratory Data Analysis")
#     st.write("We will perform some exploratory data analysis to better understand the relationships between the features.")

#     # Visualize distribution of gamma ray readings
#     st.write("Distribution of Gamma Ray Readings")
#     sns.displot(df, x="GR", bins=30)
#     st.pyplot()

#     # Visualize relationship between porosity and permeability
#     st.write("Relationship between Resistivity and Photoelectric Effect")
#     sns.scatterplot(data=df, x="ILD_log10", y="PE", hue="DeltaPHI", palette="coolwarm")
#     st.pyplot()

#     st.header("Predictive Modeling")
#     st.write("We will build a predictive model to estimate oil and gas presence based on the other features in the data.")

#     # Train predictive model
#     # ...

#     st.header("Conclusion")
#     st.write("In this analysis, we explored the well log data and performed some initial data cleaning and exploratory data analysis. We also built a predictive model to estimate oil saturation based on the other features in the data.")

#     st.write("Further analysis could include more advanced feature engineering, model selection, and hyperparameter tuning to improve the accuracy of the predictive model.")






























































'''import streamlit as st
import os 
# The OS module in Python provides functions for interacting with the operating system. 
import streamlit as st
# EDA packages : Exploitary data analysis
import pandas as pd
# Viz packages : Visualization packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # To help us to prevent erros while trying to plot
# The canonical renderer for user interfaces is Agg which uses the Anti-Grain Geometry C++ library to make a raster (pixel) image of the figure.
# Like in tiknter it is matplotlib.use('TkAgg')
import seaborn as sns

def load_view():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    """EDA toolkit"""
    st.title("Exploratory Data Analysis")
    st.subheader("Simple Data Science Explorer with Streamlit")
    
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
        .css-6qob1r{
            background-image: url("https://wallpaperaccess.com/full/2941149.jpg");
            background-size: cover;
            }
    </style>""", unsafe_allow_html=True)

    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    # def file_selector(folder_path='./apps/datasets'): # current
    #     filenames=os.listdir(folder_path)
    #     selected_filename = st.selectbox("Select A file",filenames)
    #     return os.path.join(folder_path,selected_filename)
   
    filename = uploaded_file
    st.info("You Selected {}".format(filename))
  
    # Read Data
    if uploaded_file is not None:
        df = pd.read_csv(filename)
        st.markdown("Glimpse of dataset")
    else:
        # st.write("Awaiting")
        pass

    # Show Dataset
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to View",0,1000) #Upper limit and lower limit can be set.
        st.dataframe(df.head(number)) # The head() function is used to get the first n rows.

    
    # Show columns
    if st.button("Column Names"):
        st.write(df.columns)

    
    # Show Size
    if st.checkbox("Size of Dataset"):
        data_dim = st.radio("Show Dimension By",("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0]) #Pandas
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1]) # Pandas
        else:
            st.write(df.shape) 

      
    # Select Columns
    if st.checkbox("Select Columns To Show:"):
        all_columns = df.columns.tolist() #tolist(), used to convert the data elements of an array into a list.
        selected_columns = st.multiselect("Select",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)


    # Show Values
    if st.button("Value Counts"):
        st.text("Value Counts By Target/Class")
        st.write(df.iloc[:,-1].value_counts()) #value_counts() function returns object containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.
    #Python iloc() function enables us to select a particular cell of the dataset, that is, it helps us select a value that belongs to a particular row or column from a set of values of a data frame or dataset.


    # Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe().T) # Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.


    ## Plot And Visualization
    st.subheader("Data Visualization")
    # Correlation Plot
    # Seaborn 
     
    if st.checkbox("Correlation Plot[Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True)) #Python seaborn has the power to show a heat map using its special function sns.heatmap().
        # If True, write the data value in each cell
        st.pyplot() #pyplot is a collection of functions that make matplotlib work like MATLAB.

    # Count Plot

    if st.checkbox("Plot Of Value Counts"):
        st.text("Value Counts By Targe")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary column to GroupBy",all_columns_names)
        selected_columns_names = st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()

    # Pie Chart

    if st.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate Pie Plot"):
            st.success("Generating A pie Plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%")) #autopct enables you to display the percent value using Python string formatting.
            st.pyplot()

    # Customizable Plot
    if st.checkbox("Customize Plot"):
        st.subheader('Customizable Plot')
        all_columns_names = df.columns.tolist()
        type_of_plots = st.selectbox('Select Type of Plot',["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select columns to plot",all_columns_names)


    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot {} for {}".format(type_of_plots,selected_columns_names))
        
        # Plot By Streamlit
        if type_of_plots == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)
        elif type_of_plots == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)
        elif type_of_plots == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)
        # Custom By 
        elif type_of_plots:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plots)
            st.write(cust_plot)
            st.pyplot()

# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
# if __name__ == '__main__':
#     main()'''
