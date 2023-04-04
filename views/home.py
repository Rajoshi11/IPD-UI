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
import base64
from PIL import Image

def load_view():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # page_bg_img = f"""
    # <style>
    # [data-testid="stAppViewContainer"] > .main {{
    # background-image: url("https://unsplash.com/photos/XLFu0PM5Qsg");
    # }}
    # """
    # st.markdown(page_bg_img, unsafe_allow_html=True)
    col1, col2, col3 = st.columns((2,7,1))
    with col2:
        st.title("APPLICATION OF ML IN FACIES CLASSIFICATION")
        # st.subheader("Problem definition:" )
    st.markdown("#")
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
    </style>""", unsa fe_allow_html=True)

    col1, col2 = st.columns((2,3))
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
    st.image(image, caption='System architecture and Block Diagram  ', width=1400)
    # with st.sidebar.header('1. Upload your CSV data'):
    #     uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    # # def file_selector(folder_path='./apps/datasets'): # current
    # #     filenames=os.listdir(folder_path)
    # #     selected_filename = st.selectbox("Select A file",filenames)
    # #     return os.path.join(folder_path,selected_filename)
   
    # filename = uploaded_file
    # st.info("You Selected {}".format(filename))
  
    # # Read Data
    # if uploaded_file is not None:
    #     df = pd.read_csv(filename)
    #     st.markdown("Glimpse of dataset")
    # else:
    #     # st.write("Awaiting")
    #     pass

#     # Show Dataset
#     if st.checkbox("Show Dataset"):
#         number = st.number_input("Number of Rows to View",0,1000) #Upper limit and lower limit can be set.
#         st.dataframe(df.head(number)) # The head() function is used to get the first n rows.

    
#     # Show columns
#     if st.button("Column Names"):
#         st.write(df.columns)

    
#     # Show Size
#     if st.checkbox("Size of Dataset"):
#         data_dim = st.radio("Show Dimension By",("Rows","Columns"))
#         if data_dim == 'Rows':
#             st.text("Number of Rows")
#             st.write(df.shape[0]) #Pandas
#         elif data_dim == 'Columns':
#             st.text("Number of Columns")
#             st.write(df.shape[1]) # Pandas
#         else:
#             st.write(df.shape) 

      
#     # Select Columns
#     if st.checkbox("Select Columns To Show:"):
#         all_columns = df.columns.tolist() #tolist(), used to convert the data elements of an array into a list.
#         selected_columns = st.multiselect("Select",all_columns)
#         new_df = df[selected_columns]
#         st.dataframe(new_df)


#     # Show Values
#     if st.button("Value Counts"):
#         st.text("Value Counts By Target/Class")
#         st.write(df.iloc[:,-1].value_counts()) #value_counts() function returns object containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.
#     #Python iloc() function enables us to select a particular cell of the dataset, that is, it helps us select a value that belongs to a particular row or column from a set of values of a data frame or dataset.


#     # Show Summary
#     if st.checkbox("Summary"):
#         st.write(df.describe().T) # Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.


#     ## Plot And Visualization
#     st.subheader("Data Visualization")
#     # Correlation Plot
#     # Seaborn 
     
#     if st.checkbox("Correlation Plot[Seaborn]"):
#         st.write(sns.heatmap(df.corr(),annot=True)) #Python seaborn has the power to show a heat map using its special function sns.heatmap().
#         # If True, write the data value in each cell
#         st.pyplot() #pyplot is a collection of functions that make matplotlib work like MATLAB.

#     # Count Plot

#     if st.checkbox("Plot Of Value Counts"):
#         st.text("Value Counts By Targe")
#         all_columns_names = df.columns.tolist()
#         primary_col = st.selectbox("Primary column to GroupBy",all_columns_names)
#         selected_columns_names = st.multiselect("Select Columns",all_columns_names)
#         if st.button("Plot"):
#             st.text("Generate Plot")
#             if selected_columns_names:
#                 vc_plot = df.groupby(primary_col)[selected_columns_names].count()
#             else:
#                 vc_plot = df.iloc[:,-1].value_counts()
#             st.write(vc_plot.plot(kind="bar"))
#             st.pyplot()

#     # Pie Chart

#     if st.checkbox("Pie Plot"):
#         all_columns_names = df.columns.tolist()
#         if st.button("Generate Pie Plot"):
#             st.success("Generating A pie Plot")
#             st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%")) #autopct enables you to display the percent value using Python string formatting.
#             st.pyplot()

#     # Customizable Plot

#     if st.checkbox("Customizable Plot"):
#         st.subheader('Customizable Plot')
#         all_columns_names = df.columns.tolist()
#         type_of_plots = st.selectbox('Select Type of Plot',["area","bar","line","hist","box","kde"])
#         selected_columns_names = st.multiselect("Select columns to plot",all_columns_names)
#     else:
#         pass


#     if st.button("Generate Plot"):
#         st.success("Generating Customizable Plot {} for {}".format(type_of_plots,selected_columns_names))
        
#         # Plot By Streamlit
#         if type_of_plots == 'area':
#             cust_data = df[selected_columns_names]
#             st.area_chart(cust_data)
#         elif type_of_plots == 'bar':
#             cust_data = df[selected_columns_names]
#             st.bar_chart(cust_data)
#         elif type_of_plots == 'line':
#             cust_data = df[selected_columns_names]
#             st.line_chart(cust_data)
#         # Custom By 
#         elif type_of_plots:
#             cust_plot = df[selected_columns_names].plot(kind=type_of_plots)
#             st.write(cust_plot)
#             st.pyplot()

# # if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
# # if __name__ == '__main__':
# #     main()
