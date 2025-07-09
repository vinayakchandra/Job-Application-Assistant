import streamlit as st
from services import summarize_github_repo, generate_linkedin_post


def render():
    st.title("🔍 Summarize Github Repository")

    github_repo_link = st.text_area("Paste GitHub Repo Link")
    tab1, tab2 = st.tabs(
        ["🔍 Summarize Repo", "🔗 Linkedin Post"]
    )
    with tab1:
        if st.button("Summarize"):
            if not github_repo_link.strip():
                st.warning("Please paste Github link first!")
            else:
                with st.spinner("Summarizing..."):
                    st.session_state.summarize = summarize_github_repo(github_repo_link)
                st.success("summarized successfully!")

            if st.session_state.summarize:
                st.markdown("### Repo Description:")
                st.markdown(st.session_state.summarize)
    with tab2:
        if st.button("Generate Post"):
            if not github_repo_link.strip():
                st.warning("Please paste Github link first!")
            else:
                with st.spinner("Generating Post..."):
                    st.session_state.linkedin_post = generate_linkedin_post(github_repo_link)
                st.success("Generating Post successfully!")

            if st.session_state.linkedin_post:
                st.markdown("### 🔗 Linkedin Post:")
                st.markdown(st.session_state.linkedin_post)
