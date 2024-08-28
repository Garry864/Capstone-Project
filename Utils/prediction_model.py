import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.preprocessing import StandardScaler
from streamlit_lottie import st_lottie
from dotenv import load_dotenv
load_dotenv()


animation = os.getenv("PREDICTION_URL") or st.secrets["PREDICTION_URL_st"]
 

# Load the trained model

@st.cache_resource
def load_model():
    with open('saved_models/knn_model.sav', 'rb') as f:
        rf = pickle.load(f)

    with open('saved_models/knn_model.sav', 'rb') as f:
        knn = pickle.load(f)

    with open('saved_models/xgb_model.sav', 'rb') as f:
        xgb = pickle.load(f)

    # Load the scaler
    with open('saved_models/sd.sav', 'rb') as f:
        sd = pickle.load(f)

    # Load the model columns
    with open('saved_models/dummy_columns.sav', 'rb') as f:
        dummy_columns = pickle.load(f)

    Model = {"rf": rf, "knn": knn, "xgb": xgb, "sd": sd, "dummy_cols": dummy_columns}
    return Model

Models = load_model()

knn = Models["knn"]
rf = Models["rf"]
xgb = Models["xgb"]
sd = Models["sd"]
dummy_columns = Models["dummy_cols"]


# Define preprocessing functions
def preprocess_input(data):
    # Replace values in 'fuel', 'seller_type', 'owner'
    data['fuel'] = data['fuel'].replace({'CNG': 'other', 'LPG': 'other', 'Electric': 'other'})
    data['seller_type'] = data['seller_type'].replace({'Trustmark Dealer': 'Other Dealer', 'Dealer': 'Other Dealer'})
    data['owner'] = data['owner'].replace({'Third Owner': 'Other Owner', 'Fourth & Above Owner': 'Other Owner', 'Test Drive Car': 'Other Owner'})

    # Standardize numerical columns
    num_cols = ['year', 'km_driven']
    data[num_cols] = sd.transform(data[num_cols])

    # Convert categorical variables into dummies
    data = pd.get_dummies(data)

    # Align the columns with the model's expectations
    # Create a DataFrame with model_columns and fill missing columns with zeros
    data = data.reindex(columns=dummy_columns, fill_value=0)
    
    return data

@st.fragment
def display_result(options, Feature):
    show_results(options, Feature)
    st.balloons()


@st.dialog("Prediction results")
def show_results(options, Feature):
    # st.write(Feature)

    if st_lottie(animation, 
            key="prd",
            height = 230,
            width = None       
        ):
    

        if Feature is not None:
                
            if options == 'Random Forest':
                prediction = rf.predict(Feature)[0]
            elif options == 'XG-Boost':
                prediction = xgb.predict(Feature)[0]
            elif options == 'K-Neighbours':
                prediction = knn.predict(Feature)[0]
                
            st.success(f'The predicted price of the Car is: {prediction:.2f}')

    


def predict_input(options):

    col1, col2, col3 = st.columns(3, gap = 'small')

    with col1:
        brand = st.selectbox('Car Brand', ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Other'])
    with col2:
        transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    with col3:
        owner = st.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

    with col1:
        year = st.number_input('Year of Manufacture', min_value=1990, max_value=2024, step=1)
    with col2:
        fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    with col3:
        seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])

    km_driven = st.slider('Km Driven', min_value = 1, max_value = 171000, step = 10)


    # Prepare input data for preprocessing
    input_data = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel_type],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'Brand': [brand]
    })

    # Preprocess the input data
    Feature = preprocess_input(input_data)

    

    # Predict and display result
    if st.button('Predict'):

        # show_results(options, Feature)
        display_result(options, Feature)
    
