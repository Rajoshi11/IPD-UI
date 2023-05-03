import streamlit as st
import pandas as pd
import plotly.express as px

def load_view():
    st.title('Exploratory Data Analysis') 
    # Load Data
    uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV file)", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully")
        st.markdown("------")
    else:
        st.info('Awaiting for CSV file to be uploaded.')
    
    def style_df(df):
        return df.style.background_gradient(cmap='coolwarm', low=0, high=1, axis=0)
        # return df.style.set_properties(**{'background-color': '#0A4D68',
        #                                  'color': 'black',
        #                                  'border-color': 'white'})
    # Data Overview Tab
    def data_overview_tab():
        st.subheader("Data Overview")
        st.write("Displaying top few rows of the data:")
        st.dataframe(style_df(df.head()))
        st.write("Displaying data statistics:")
        st.dataframe(style_df(df.describe()))

    # Data Analysis Tab
    def data_analysis_tab():
        st.subheader("Data Analysis")
        
        # Data Visualization
        st.write("Data Visualization:")
        fig = px.scatter(df, x='Depth', y='GR', color='Facies', hover_data=['Well Name'])
        st.plotly_chart(fig)
        
        # Data Filtering
        st.write("Data Filtering:")
        formation_filter = st.multiselect("Filter by Formation", df['Formation'].unique())
        presence_filter = st.multiselect("Filter by Presence", df['Presence'].unique())
        filtered_df = df[(df['Formation'].isin(formation_filter)) & (df['Presence'].isin(presence_filter))]
        st.dataframe(filtered_df)
        
        # Data Manipulation
        st.write("Data Manipulation:")
        well_grouped_df = df.groupby('Well Name').agg({'PHIND': 'mean', 'DeltaPHI': 'mean'}).reset_index()
        st.dataframe(well_grouped_df)

    # More Tabs
    def custom_eda_tab():
        st.subheader("Custom EDA")
        
        # Custom Analysis 1
        st.write("Custom Analysis 1:")
        formation_avg_delta_phi = df.groupby('Formation')['DeltaPHI'].mean().reset_index()
        fig1 = px.bar(formation_avg_delta_phi, x='Formation', y='DeltaPHI', color='Formation',
                    title='Formation vs. Average DeltaPHI')
        st.plotly_chart(fig1)
        
        # Custom Analysis 2
        st.write("Custom Analysis 2:")
        well_phind_stats = df.groupby('Well Name')['PHIND'].describe().reset_index()
        st.dataframe(well_phind_stats)

    # Main App
    
    st.title("Exploratory Data Analysis of Oil and Gas Presence")
    st.header("Dataset")
    st.write("Our dataset contains well log data from oil and gas exploration. It includes measurements such as Gamma Ray, Resistivity, and Porosity, as well as lithology and hydrocarbon presence labels. The goal is to use this data to identify areas with high potential for oil and gas presence.")
    # Display information on the features of interest
    st.header("Features of Interest")
    st.write("In our dataset, the following features are of particular interest for identifying areas with high potential for oil and gas presence:")
    st.write("- Gamma Ray")
    st.write("- Resistivity")
    st.write("- Porosity")
    st.write("- Density")
    st.write("- Photoelectric Effect")
    st.write("- Average of neutron and density log")
    st.title("Well Log Data Analysis")

    tabs = ["Select desired tab","Data Overview", "Data Analysis", "Custom EDA"]
    tab_selected = st.sidebar.selectbox("Select a tab", tabs)
    
    if tab_selected == "Select desired tab":
        st.warning("upload the dataset")
    if tab_selected == "Data Overview":
        data_overview_tab()
    elif tab_selected == "Data Analysis":
        data_analysis_tab()
    elif tab_selected == "Custom EDA":
        custom_eda_tab()
        pass

    