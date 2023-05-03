import streamlit as st
# Libraries
import pandas as pd
import lazypredict
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io
import numpy as np
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from sklearn.preprocessing import LabelEncoder

def load_view():   
    def tab1():
        def build_model(df):
            le = LabelEncoder()
            df['Presence'] = le.fit_transform(df['Presence'])
            df['Well Name'] = le.fit_transform(df['Well Name'])
            df['Formation'] = le.fit_transform(df['Formation'])
            X = df.iloc[:,:-1] # Features variables
            Y = df.iloc[:,-1]  # Target variable

            # Dimensions of dataset
            st.markdown('**1.2. Dataset dimension**')
            st.write('X')
            st.info(X.shape)
            st.write('Y')
            st.info(Y.shape)

            # Variable details
            st.markdown('**1.3. Variable details**:')
            st.write('X variable (first 20 are shown)')
            st.info(list(X.columns[:20]))
            st.write('Y variable')
            st.info(Y.name)

            # Building lazy model
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = split_size,random_state = seed_number)
            # reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None)
            clf = LazyClassifier( verbose=0, ignore_warnings=True, custom_metric=None)
            models,predictions = clf.fit(X_train, X_test, Y_train, Y_test)
            # verbose is the choice that how you want to see the output of your algorithm while it's training
            models_train,predictions_train = clf.fit(X_train, X_train, Y_train, Y_train)
            models_test,predictions_test = clf.fit(X_train, X_test, Y_train, Y_test)
            
            st.subheader('2. Table of Model Performance')

            st.write('Training set')
            st.write(predictions_train)
            st.markdown(filedownload(predictions_train,'training.csv'), unsafe_allow_html=True)

            st.write('Test set')
            st.write(predictions_test)
            top_5 = predictions_test[:5]['Accuracy']

            # Display the list of algorithm names in the Streamlit app
            st.write(list(top_5.index))
            st.markdown(filedownload(predictions_test,'test.csv'), unsafe_allow_html=True)

            st.subheader('3. Plot of Model Performance (Test set)')

            #Accuracy
            with st.markdown('**Accuracy**'):
                # Tall
                predictions_test["Accuracy"] = [0 if i < 0 else i for i in predictions_test["Accuracy"] ]
                # if value(i) is less than 0 i.e R-squared predicted value of test set is 0 , it will return 0
                # else it will return the R-squared value predicted
                plt.figure(figsize=(3, 9))
                sns.set_theme(style="whitegrid")
                ax1 = sns.barplot(y=predictions_test.index, x="Accuracy", data=predictions_test)
                ax1.set(xlim=(0, 1))
                # xlim is basically the x axis value sepration range
            st.markdown(imagedownload(plt,'plot-r2-tall.pdf'), unsafe_allow_html=True)
                # Wide
            plt.figure(figsize=(9, 3))
            sns.set_theme(style="whitegrid")
            ax1 = sns.barplot(x=predictions_test.index, y="Accuracy", data=predictions_test)
            ax1.set(ylim=(0, 1))
            # y axis plot download
            plt.xticks(rotation=90)
            st.pyplot(plt)
            st.markdown(imagedownload(plt,'plot-r2-wide.pdf'), unsafe_allow_html=True)

            # Calculation plot
            with st.markdown('**Calculation time**'):
                # Tall
                predictions_test["Time Taken"] = [0 if i < 0 else i for i in predictions_test["Time Taken"] ]
                plt.figure(figsize=(3, 9))
                sns.set_theme(style="whitegrid")
                ax3 = sns.barplot(y=predictions_test.index, x="Time Taken", data=predictions_test)
            st.markdown(imagedownload(plt,'plot-calculation-time-tall.pdf'), unsafe_allow_html=True)
                # Wide
            plt.figure(figsize=(9, 3))
            sns.set_theme(style="whitegrid")
            ax3 = sns.barplot(x=predictions_test.index, y="Time Taken", data=predictions_test)
            plt.xticks(rotation=90)
            st.pyplot(plt)
            st.markdown(imagedownload(plt,'plot-calculation-time-wide.pdf'), unsafe_allow_html=True)
            return top_5

        def filedownload(df, filename):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
            href = f'<a href="data:file/csv;base64,{b64}" download={filename}>Download {filename} File</a>'
            return href

        def imagedownload(plt, filename):
            s = io.BytesIO()
            plt.savefig(s, format='pdf', bbox_inches='tight')
            plt.close()
            b64 = base64.b64encode(s.getvalue()).decode()  # strings <-> bytes conversions
            href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
            return href

        st.write("""
        # Auto Ml Classification App 
        """)

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

        # Sidebar - Collects user input features into dataframe
        with st.sidebar.header('1. Upload your CSV data'):
            uploaded_file = st.sidebar.file_uploader(" do Upload your input CSV file", type=["csv"])
            st.sidebar.markdown("""
        [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
        """)

        # Sidebar - Specify parameter settings
        with st.sidebar.header('2. Set Parameters'):
            split_size = st.sidebar.slider('Data split ratio is(% for Training Set)', 10, 90, 80, 5)
            seed_number = st.sidebar.slider('Set the random seed number', 1, 100, 43, 1)


        # Main Panel
        # Displays the dataset
        st.subheader('1. Dataset')

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.markdown('**1.1. Glimpse of dataset**')
            st.write(df)
            my_list = build_model(df)
            st.subheader("Top 5 Perfomace Algorithms")
            st.write(my_list)
            st.session_state.my_list = my_list
        else:
            st.info('Awaiting for CSV file to be uploaded.')
        











    #-------------------------------------TAB 2---------------------------------------------------------#










    def tab2():
        import pandas as pd
        import os
        import streamlit as st 
        st.title('Train and Download Model Weights')
        
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
            st.write(df)
            
            
            import streamlit as st
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier, BaggingClassifier
            from sklearn.linear_model import LogisticRegression
            from sklearn.svm import SVC,NuSVC,LinearSVC
            from sklearn.naive_bayes import GaussianNB,BernoulliNB
            import lazypredict
            from lazypredict.Supervised import LazyClassifier
            import pickle
            from sklearn.preprocessing import LabelEncoder
            from sklearn.tree import ExtraTreeClassifier, DecisionTreeClassifier
            from lightgbm import LGBMClassifier
            from sklearn.semi_supervised import LabelPropagation, LabelSpreading
            from sklearn.neighbors import NearestNeighbors,NearestCentroid
            from sklearn.calibration import CalibratedClassifierCV
            from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,QuadraticDiscriminantAnalysis
            from sklearn.linear_model import SGDClassifier,PassiveAggressiveClassifier,RidgeClassifier,RidgeClassifierCV,Perceptron
            from sklearn.dummy import DummyClassifier


            # Load the well log dataset
            le = LabelEncoder()
            df['Presence'] = le.fit_transform(df['Presence'])
            df['Well Name'] = le.fit_transform(df['Well Name'])
            df['Formation'] = le.fit_transform(df['Formation'])
            X = df.iloc[:,:-1] # Features variables
            y = df.iloc[:,-1]  # Target variable
            # Define the X and y variables


            # Split the dataset into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


            # Define the classification algorithms to consider
            algorithms = {
                'RandomForestClassifier': RandomForestClassifier(),
                'XGBClassifier': GradientBoostingClassifier(),
                'Logistic Regression': LogisticRegression(),
                'SVM': SVC(),
                'Naive Bayes': GaussianNB(),
                'AdaBoostClassifier' : AdaBoostClassifier(),
                'ExtraTreesClassifier' : ExtraTreesClassifier(),
                'BaggingClassifier' : BaggingClassifier(),
                'ExtraTreeClassifier' : ExtraTreeClassifier(),
                'LGBMClassifier' : LGBMClassifier(),
                'DecisionTreeClassifier' : DecisionTreeClassifier(),
                'LabelPropagation' : LabelPropagation(),
                'LabelSpreading' : LabelSpreading(),
                'NearestNeighbors' : NearestNeighbors(),
                'NuSVC' : NuSVC(),
                'LinearSVC' : LinearSVC(),
                'CalibratedClassifierCV' : CalibratedClassifierCV(),
                'BernoulliNB' : BernoulliNB(),
                'LinearDiscriminantAnalysis' : LinearDiscriminantAnalysis(),
                'SGDClassifier' : SGDClassifier(),
                'PassiveAggressiveClassifier' : PassiveAggressiveClassifier(),
                'RidgeClassifier' : RidgeClassifier(),
                'RidgeClassifierCV' : RidgeClassifierCV(),
                'Perceptron' : Perceptron(),
                'NearestCentroid' : NearestCentroid(),
                'QuadraticDiscriminantAnalysis' : QuadraticDiscriminantAnalysis(),
                'DummyClassifier' : DummyClassifier()
            }


            # Define function to train and save the model weights for a given algorithm
            def train_model(algorithm):
                clf = algorithm.fit(X_train, y_train)
                model_file = open(f"{algorithm.__class__.__name__}.pkl", "wb")
                pickle.dump(clf, model_file)
                model_file.close()
                return clf


           
                
                
            # Allow user to select a classification algorithm from a dropdown menu
            # selected_algorithm_names = ['Logistic Regression', 'Random Forest','DummyClassifier','PassiveAggressiveClassifier']
            my_list = st.session_state.my_list
            st.subheader("Top 5 Performance Algorithms")
            st.write(my_list)
            selected_algorithm_dict = dict(filter(lambda x: x[0] in my_list, algorithms.items()))
            selected_algorithm = st.selectbox('Select an algorithm', list(selected_algorithm_dict.keys()))
            
            # Train the selected algorithm and display its accuracy
            st.write(f"Training {selected_algorithm}...")
            clf = train_model(algorithms[selected_algorithm])
            accuracy = clf.score(X_test, y_test)
            st.write(f"{selected_algorithm}: Accuracy - {accuracy}")
            
            # Allow user to download the trained weights pickle file
            file_name = f"{selected_algorithm}.pkl"
            file_bytes = pickle.dumps(clf)
            st.download_button(
                label="Download Trained Weights",
                data=file_bytes,
                file_name=file_name,
                mime="application/octet-stream"
            )
        else:
            st.info('Awaiting for CSV file to be uploaded.')























    #------------------------------------------------TAB3-----------------------------------------#
    def tab3():
        import pandas as pd
        import os
        import streamlit as st 
        st.title('Predictive Model: Make Data-Driven Predictions with Trained Weights')
        
        uploaded_file = st.sidebar.file_uploader("Choose the file for this")

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
            import pickle
            le = LabelEncoder()
            df['Well Name'] = le.fit_transform(df['Well Name'])
            df['Formation'] = le.fit_transform(df['Formation'])
            st.subheader("Upload the pickle file of trained model")
            model_file = st.file_uploader("Upload a trained model (pickle file)", type=["pkl"])
            st.markdown("-------------")
            if model_file is not None:
                model = pickle.load(model_file)
                predictions = model.predict(df)
                # define the mapping between numbers and categories
                mapping = {0: "Low", 1: "Medium", 2: "High"}

                # create a Pandas Series from the numerical array
                series = pd.Series(predictions)

                # use the map() method to apply the mapping to the series
                categories = series.map(mapping)
                col1, col2 = st.columns(2)
                # Display the dataframes in separate columns
                with col1:
                    st.subheader("Predicted (encoded) target variable")
                    st.write(predictions)

                with col2:
                    st.subheader("Predicted Presence of Oil and gas")
                    st.write(categories)
                st.markdown("-------------")
                
                # concatenated_df = pd.concat([df,categories.to_frame()], axis=0, ignore_index=True)
                # st.write("Concatenated Dataframe:")
                # st.write(concatenated_df)
                if st.button('Download DataFrame'):
                    # convert the DataFrame to a CSV file and download it
                    csv = categories.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="Predicted presence of oil and gas.csv">Download CSV file</a>'
                    st.markdown(href, unsafe_allow_html=True)


        else:
            st.info('Awaiting for CSV file to be uploaded.')
            














































    #-------------------------------------ENDS---------------------------------------------#






    tabs = ["AutoML Classification", "Training", "Prediction"]
    current_tab = st.sidebar.selectbox("Select a tab", tabs)

    if current_tab == "AutoML Classification":
        tab1()
    elif current_tab == "Training":
        tab2()
    else:
        tab3()

        