import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import base64

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# with open('My_capstone_project.pdf', 'rb') as f:
#     pdf_file = f.read()

def autoviz_html(file_name, width = 1000, height = 500):
    with open(f"AutoViz_Plots/AutoViz/{file_name}.html", "r", encoding='ISO-8859-1') as file:
        html_content = file.read()

    components.html(html_content, width=width, height=height, scrolling=True)

@st.dialog("Data Analysis", width="large")
def show_pdf(file):
    pdf_contents = file.read()
    base64_pdf = base64.b64encode(pdf_contents).decode('utf-8')
    pdf_display = f'<iframe src = "data:application/pdf;base64,{base64_pdf}" width = "700 " height = "800" type = "application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def descprit_data(df):

    with st.expander('descriptions'):
         # Create multiple check box in row
        col_name, col_dtype, col_data = st.columns(3)

        # Create a checkbox to get the summary.
        # with veiw_summary:
        if st.checkbox("View Summary"):
            st.dataframe(df.describe(), use_container_width=True)

        # Create multiple check box in row

       

        # Show name of all dataframe
        with col_name:
            if st.checkbox("Column Names"):
                st.dataframe(df.columns, use_container_width=True)

        # Show datatype of all columns 
        with col_dtype:
            if st.checkbox("Columns data types"):
                dtypes = df.dtypes.apply(lambda x: x.name)
                st.dataframe(dtypes, use_container_width=True)
        
        # Show data for each columns
        with col_data: 
            if st.checkbox("Columns Data"):
                col = st.selectbox("Column Name", list(df.columns))
                st.dataframe(df[col].head(8), use_container_width=True)

