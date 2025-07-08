import streamlit as st
from components import job_assistant


def init_session_state():
    defaults = {
        "cover_letter": "",
        "project_ideas": "",
        "job_info": "",
        "tech_stack": "",
        "resume": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()

st.sidebar.title("🧭 Navigation")
page = st.sidebar.selectbox("",["🚀Job Application Assistant"])

if page == "🚀Job Application Assistant":
    job_assistant.render()
