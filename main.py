from collections.abc import Iterable
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

# Initialize session state
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""
if "project_ideas" not in st.session_state:
    st.session_state.project_ideas = ""
if "job_info" not in st.session_state:
    st.session_state.job_info = ""
if "tech_stack" not in st.session_state:
    st.session_state.tech_stack = ""
if "resume" not in st.session_state:
    st.session_state.resume = ""


def call_groq(job_description, prompt):
    msgs: Iterable = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": f"Job Description: {job_description}",
        }
    ]

    return client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=msgs,
        temperature=0.5,
    )


def generate_cover_letter(job_description: str, resume: str):
    prompt = (
        "You are an expert cover-letter builder. Tailor a cover letter for the role below. "
        "Generate the cover letter in a concise and professional way. "
        "Give suggestions for adding Resume, Portfolio website, Github, Linkedin, etc. Make a divider before suggestions. "
        "use resume data "
        f"RESUME: {resume}"
    )

    chat_completion = call_groq(job_description, prompt)
    return chat_completion.choices[0].message.content


def project_ideas(job_description: str):
    prompt = (
        "You are excellent at suggesting project ideas based on job descriptions. "
        "Suggest useful projects someone could do to match this job description. Also tell difficulty levels"
        "use emojicons"
    )

    chat_completion = call_groq(job_description, prompt)
    return chat_completion.choices[0].message.content


def job_info(job_description: str):
    prompt = (
        "You are excellent at finding job insights based on job descriptions. "
        "Give job insights. use emojicons."
    )

    chat_completion = call_groq(job_description, prompt)
    return chat_completion.choices[0].message.content


def getTechStack(job_description: str):
    prompt = (
        "Get All the Tech Stack and tools used or will be required for doing this job. Add emojicons"
    )

    chat_completion = call_groq(job_description, prompt)
    return chat_completion.choices[0].message.content


def compare_with_resume(job_description: str, resume: str):
    prompt = (
        "Compare user's Resume with Job Description and give all the insights if he is eligible for the job or not."
        "use emojicons like ticks and cross"
        f"Resume: {resume}"
    )

    chat_completion = call_groq(job_description, prompt)
    return chat_completion.choices[0].message.content


# Streamlit UI
st.set_page_config(page_title="AI Cover Letter & Project Helper", layout="centered")
st.title("🚀 Job Application Assistant")

job_description = st.text_area("Paste your Job Description", height=250)
resume = st.text_area("Paste your Resume", height=200)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📄 Cover Letter", "💡 Project Ideas", "🔍 Job Insights", "🖥️ Tech Stack", "🔄 Compare with Resume"])

# Cover Letter
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
# Project Ideas
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
# Job Insights
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
# Tech Stack
with tab4:
    if st.button("Get Tech Stack"):
        if not job_description.strip():
            st.warning("Please paste a job description first!")
        else:
            with st.spinner("Getting Tech Stack..."):
                st.session_state.tech_stack = getTechStack(job_description)
            st.success("Generated!")

    if st.session_state.tech_stack:
        st.markdown("### Tech Stack:")
        st.markdown(st.session_state.tech_stack)
# Resume
with tab5:
    if st.button("compare"):
        if not job_description.strip():
            st.warning("Please paste a job description first!")
        if not resume.strip():
            st.warning("Please put your resume first!")
        else:
            with st.spinner("Comparing job description with your Resume..."):
                st.session_state.resume = compare_with_resume(job_description, resume)
            st.success("Generated!")

    if st.session_state.resume:
        st.markdown("### Compare with Resume:")
        st.markdown(st.session_state.resume)
