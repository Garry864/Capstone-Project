import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
from streamlit_extras.dataframe_explorer import dataframe_explorer

# --------------PAGE SETTINGS--------------------

st.set_page_config(page_title="Capstone Project",
                   layout="wide",
                   page_icon="🤖")
# --------------------------------------------------

from Utils.prediction_model import *
from Utils.visualization import *
from Utils.data_info import *
from Utils.about_me import *

# ------------------------------------------------------


# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))


# --- Heading ---
st.markdown(
    """
    <style>
        .heading-container {
            background: linear-gradient(135deg, #d33682, #3a4b4f);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
            margin-bottom: 20px;
        }
        .heading-container h1 {
            font-size: 36px;
            font-family: 'Helvetica', sans-serif;
            margin: 0;
            color: #fff;
        }
        .heading-container p {
            font-size: 18px;
            font-family: 'Helvetica', sans-serif;
            margin-top: 5px;
            color: #d1d1d1;
        }
    </style>
    <div class="heading-container">
        <h1>Welcome to the Car Price Prediction App</h1>
        <p>Utilize cutting-edge machine learning models to predict car prices with ease.</p>
    </div>
    """,
    unsafe_allow_html=True
)

Prediction, Data_info, Visualization, contact_info = st.tabs(["Prediction", "Dataset Overview", "Visualization", "Contact Info"])


st.sidebar.header("Machine Learning Prediction :material/psychology:")

with Prediction:

    # Title and header

    st.header('watch the presentation and fill the results for Prediction', anchor=False)



    # ppt = """
    #     <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRjyiYzrwAk1k0KMe_xuazejngWVlQo485K0DEa8maduD7nI80cTNIr_IR8ZAQqGg/embed?start=false&loop=false&delayms=3000" frameborder="0" width="1125" height="675" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    # """

    # st.markdown(ppt, unsafe_allow_html=True)

    st.video("assets/presentation.mp4", 
             loop = True,
             autoplay = True,
             muted = True
             )

    # sidebar for navigation
    with st.sidebar:
        selected = option_menu('Select The Model',

                            ['Random Forest',
                            'K-Neighbours',
                            'XG-Boost'],
                            # menu_icon='hospital-fill',
                            icons=['bi-tree', 'heart', 'activity'],
                            default_index=0)

    st.success(f'Your selected Model is {selected}')

    predict_input(selected)
    st.divider()


# Footer

# "---"
st.sidebar.markdown("---")

st.sidebar.caption("Accurate car price predictions with cutting-edge ML models. :car: :rocket:")

st.sidebar.caption(
    "Like this? [Hire me!](https://www.linkedin.com/in/analyst-gaurav-yadav/)"
)

st.sidebar.text("Built with ❤️ by Gaurav Yadav")


linkedin = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/linkedin.gif"
topmate = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/topmate.gif"
email = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/email.gif"
newsletter = (
    "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/newsletter.gif"
)
share = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/share.gif"

uptime = "https://uptime.betterstack.com/status-badges/v1/monitor/196o6.svg"

st.sidebar.caption(
    f"""
        <div style='display: flex; align-items: center;'>
            <a href = 'https://www.linkedin.com/in/analyst-gaurav-yadav/'><img src='{linkedin}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
            <a href = ''><img src='{topmate}' style='width: 32px; height: 32px; margin-right: 25px;'></a>
            <a href = 'mailto:Gaurav7869@outlook.com'><img src='{email}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            <a href = 'https://www.linkedin.com'><img src='{newsletter}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            <a href = 'https://www.kaggle.com/gaurav86451'><img src='{share}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            
        </div>
        <br>
        <a href = ''><img src='{uptime}'></a>
        
        """,
    unsafe_allow_html=True,
)



with Data_info:

    st.title("Data Info page", anchor=False)

    if st.button("View Jupyter file", key="jpt", help="click here to see jupyter notebook"):
        with open('assets/colab_file.pdf', 'rb') as f:
            show_pdf(f)


    

    st.markdown(
        """
        ## 📊 **Dataset Overview**

        The dataset contains various features related to used cars. Here’s a detailed description:

        - **`name`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[41]
            - **Range**: :grey[N/A]
            - **DQ Issue**: :green[No data quality issues.]

        - **`year`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[0]
            - **Range**: :grey[1992 to 2020]
            - **DQ Issue**: :red[Potential date-time column; consider transforming it before modeling.]

        - **`selling_price`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[12]
            - **Range**: :grey[20,000 to 8,900,000]
            - **DQ Issue**: :red[Contains 170 outliers. Consider capping or removing these outliers to improve accuracy.]

        - **`km_driven`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[21]
            - **Range**: :grey[1 to 806,599]
            - **DQ Issue**: :red[Contains 106 outliers. Cap or remove these outliers to ensure reliable predictions.]

        - **`fuel`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[2 rare categories: `LPG`, `Electric`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to simplify the analysis.]

        - **`seller_type`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[1 rare category: `Trustmark Dealer`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to avoid potential bias.]

        - **`transmission`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[No issue]
            
        - **`owner`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[1 rare category: `Test Drive Car`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to ensure consistency.]

        **Notes**: Address outliers and handle rare categories appropriately to enhance the dataset’s quality and improve model performance. 🚗🔍
        """,
        unsafe_allow_html=True
    )

    with st.expander("View Raw data"):
            df = pd.read_csv(f'{working_dir}/dataset/CAR DETAILS.csv')
            st.dataframe(df)
            st.subheader("This is Raw Dataset Befor Preprocessing")

    with st.expander("View Clean data"):
            df = pd.read_csv(f'{working_dir}/dataset/CAR_DETAILS_clean.csv')
            st.dataframe(df)
            st.subheader("This is Raw Dataset Befor Preprocessing")



    descprit_data(df)

    chart_list = ["Cat Plot", "Displot", "Heatmap", "Scatter Plot", "Time Series", "Violin Plot"]
    default_file = "violinplots"

    chart_mapping = {
        "Cat Plot": "cat_var_plots",
        "Displot": "distplots_nums",
        "Heatmap": "heatmaps",
        "Scatter Plot": "pair_scatters",
        "Time Series": "timeseries_plots",
    }

    with st.expander("More info", expanded=True):
        selected_charts = st.multiselect("", chart_list, placeholder="Choose your chart...")

        with st.spinner("Generating Charts..."):
            if selected_charts:
                for chart in selected_charts:
                    file_name = chart_mapping.get(chart, default_file)
                    autoviz_html(file_name)
            else:
                autoviz_html(default_file)



with Visualization:
    vizual_data()


with contact_info:
    my_page()




