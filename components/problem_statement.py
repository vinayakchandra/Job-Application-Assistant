import streamlit as st
from services import generate_ideas_from_problem_statement


def render():
    st.title("🤨 Generate Ideas from Problem Statement")

    problem_statement = st.text_area("Paste Problem Statement", height=250)

    if st.button("Generate Project Ideas"):
        if not problem_statement.strip():
            st.warning("Please paste a job description first!")
        else:
            with st.spinner("Thinking of ideal projects..."):
                st.session_state.problem_statement_ideas = generate_ideas_from_problem_statement(problem_statement)
            st.success("Project ideas generated!")

    if st.session_state.problem_statement_ideas:
        st.markdown("### Recommended Projects:")
        st.markdown(st.session_state.problem_statement_ideas)
