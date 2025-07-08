import streamlit as st
from services import *

def render():
    st.title("🚀 Job Application Assistant")

    job_description = st.text_area("Paste your Job Description", height=250)
    resume = st.text_area("Paste your Resume", height=200)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📄 Cover Letter", "💡 Project Ideas", "🔍 Job Insights", "🖥️ Tech Stack", "🔄 Compare with Resume"]
    )

    with tab1:
        if st.button("Generate Cover Letter"):
            if not job_description.strip():
                st.warning("Please paste a job description first!")
            else:
                with st.spinner("Generating your personalized cover letter..."):
                    st.session_state.cover_letter = generate_cover_letter(job_description, resume)
                st.success("Cover letter generated!")

        if st.session_state.cover_letter:
            st.markdown("### Cover Letter:")
            st.markdown(st.session_state.cover_letter)

    with tab2:
        if st.button("Generate Project Ideas"):
            if not job_description.strip():
                st.warning("Please paste a job description first!")
            else:
                with st.spinner("Thinking of ideal projects..."):
                    st.session_state.project_ideas = project_ideas(job_description)
                st.success("Project ideas generated!")

        if st.session_state.project_ideas:
            st.markdown("### Recommended Projects:")
            st.markdown(st.session_state.project_ideas)

    with tab3:
        if st.button("Get Insights"):
            if not job_description.strip():
                st.warning("Please paste a job description first!")
            else:
                with st.spinner("Getting Insights..."):
                    st.session_state.job_info = job_info(job_description)
                st.success("Job Insights generated!")

        if st.session_state.job_info:
            st.markdown("### Job Insights:")
            st.markdown(st.session_state.job_info)

    with tab4:
        if st.button("Get Tech Stack"):
            if not job_description.strip():
                st.warning("Please paste a job description first!")
            else:
                with st.spinner("Getting Tech Stack..."):
                    st.session_state.tech_stack = get_tech_stack(job_description)
                st.success("Generated!")

        if st.session_state.tech_stack:
            st.markdown("### Tech Stack:")
            st.markdown(st.session_state.tech_stack)

    with tab5:
        if st.button("Compare"):
            if not job_description.strip():
                st.warning("Please paste a job description first!")
            elif not resume.strip():
                st.warning("Please put your resume first!")
            else:
                with st.spinner("Comparing job description with your Resume..."):
                    st.session_state.resume = compare_with_resume(job_description, resume)
                st.success("Generated!")

        if st.session_state.resume:
            st.markdown("### Compare with Resume:")
            st.markdown(st.session_state.resume)
