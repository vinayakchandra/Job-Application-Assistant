import streamlit as st
from components import job_assistant, summarize, problem_statement


def init_session_state():
    defaults = {
        "cover_letter": "",
        "project_ideas": "",
        "job_info": "",
        "tech_stack": "",
        "resume": "",
        "summarize": "",
        "linkedin_post": "",
        "problem_statement_ideas": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()
pages = ["🚀Job Application Assistant", "🔍Github", "🤨Problem Statement"]

st.sidebar.title("🧭 Navigation")
page = st.sidebar.selectbox("Pages", pages)

if page == "🚀Job Application Assistant":
    job_assistant.render()
if page == "🔍Github":
    summarize.render()
if page == "🤨Problem Statement":
    problem_statement.render()
