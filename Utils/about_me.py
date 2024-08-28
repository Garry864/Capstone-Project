import streamlit as st
from forms.contact import *
from streamlit_lottie import st_lottie 
import json
import requests
from dotenv import load_dotenv

# load enviornment variables
load_dotenv()

def pass_urls():
    WEBHOOK_URL = os.getenv("WEBHOOK_URL") or st.secrets["WEBHOOK_URL_st"]
    W_URL = os.getenv("W_URL") or st.secrets["W_URL_st"]
    Work_url = os.getenv("WORK_URL") or st.secrets["WORK_URL_st"]
    Skill_url = os.getenv("SKILL_URL") or st.secrets["SKILL_URL_st"]
    Comedy = os.getenv("COMEDY_URL") or st.secrets["COMEDY_URL_st"]
    animation = os.getenv("PREDICTION_URL") or st.secrets["PREDICTION_URL_st"]

    return {
        "WEBHOOK_URL": WEBHOOK_URL,
        "W_URL": W_URL,
        "WORK_URL": Work_url,
        "SKILL_URL": Skill_url,
        "COMEDY": Comedy,
        "ANIMATION": animation
    }

# Store URLs in global variables
urls = pass_urls()


WEBHOOK_URL = urls["WEBHOOK_URL"]
W_URL = urls["W_URL"]
Work_url = urls["WORK_URL"]
Skill_url = urls["SKILL_URL"]
smiley = urls["COMEDY"]
animation = urls["ANIMATION"]



@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

def load_lottiefile(filepath: str):
    with open(filepath , 'r') as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- HERO SECTION ---

def my_page():
    col1, col2 = st.columns(2, gap = "small", vertical_alignment="center")

    with col1:
        st.image("assets/profile_photo.png", width=250)
    with col2:
        st.title("Gaurav yadav", anchor=False)
        st.write(
            "Aspiring Data Analyst, assisting enterprises by supporting data-driven decision-making."
        )
        if st.button("✉️ contact me", key="k1"):
            show_contact_form()

    # --- EXPERIENCE & QUALIFICATIONS ---
    colA, colB = st.columns(2, gap = "small", vertical_alignment="top")

    with colA:
        st.write("\n")
        st.subheader("Experience & Qualifications", anchor=False)
        st.write(
            """
            - Real world experience of extracting actionable insights from data
            - Strong hands-on experience and knowledge in Python and Excel
            - Good understanding of statistical principles and their respective applications
            - Excellent team-player and displaying a strong sense of initiative on tasks
            """
        )

        # --- SKILLS ---
        st.write("\n")
        st.subheader("Hard Skills", anchor=False)
        st.write(
            """
            - Programming: Python (Scikit-learn, Pandas), SQL, VBA
            - Data Visualization: PowerBi, MS Excel, Plotly
            - Modeling: Logistic regression, linear regression, decision trees
            - Databases: Postgres, MySQL, ChromaDB
            """
        )

    with colB:
        
        lottie_work = load_lottieurl(Work_url)
        lottie_skill = load_lottieurl(Skill_url)
        comedy = load_lottieurl(smiley)

        st_lottie(
            lottie_work,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=210,
            width=None
        )

        st_lottie(lottie_skill, 
            key="hello",
            height = 230,
            width = None
            
        )
    
    st.divider()