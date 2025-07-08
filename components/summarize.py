import streamlit as st
from services import summarize_github_repo


def render():
    st.title("🔍 Summarize Github Repository")

    github_repo_link = st.text_area("Paste GitHub Repo Link")
    if st.button("Summarize"):
        if not github_repo_link.strip():
            st.warning("Please paste a job description first!")
        else:
            with st.spinner("Summarizing..."):
                st.session_state.summarize = summarize_github_repo(github_repo_link)
            st.success("summarized successfully!")

        if st.session_state.summarize:
            st.markdown("### Repo Description:")
            st.markdown(st.session_state.summarize)
