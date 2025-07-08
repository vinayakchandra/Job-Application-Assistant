from collections.abc import Iterable

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()


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


def get_tech_stack(job_description: str):
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
