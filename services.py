import os
import tempfile
from collections.abc import Iterable

import git
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()


def make_msg_from_prompt(job_description, prompt):
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

    return call_groq(msgs)


def call_groq(msgs):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=msgs,
        temperature=0.5
    )
    return completion


def generate_cover_letter(job_description: str, resume: str):
    prompt = (
        "You are an expert cover-letter builder. Tailor a cover letter for the role below. "
        "Generate the cover letter in a concise and professional way. "
        "Give suggestions for adding Resume, Portfolio website, Github, Linkedin, etc. Make a divider before suggestions. "
        "use resume data "
        f"RESUME: {resume}"
    )

    chat_completion = make_msg_from_prompt(job_description, prompt)
    return chat_completion.choices[0].message.content


def project_ideas(job_description: str):
    prompt = (
        "You are excellent at suggesting project ideas based on job descriptions. "
        "Suggest useful projects someone could do to match this job description. Also tell difficulty levels"
        "use emojicons"
    )

    chat_completion = make_msg_from_prompt(job_description, prompt)
    return chat_completion.choices[0].message.content


def job_info(job_description: str):
    prompt = (
        "You are excellent at finding job insights based on job descriptions. "
        "Give job insights. use emojicons."
    )

    chat_completion = make_msg_from_prompt(job_description, prompt)
    return chat_completion.choices[0].message.content


def get_tech_stack(job_description: str):
    prompt = (
        "Get All the Tech Stack and tools used or will be required for doing this job. Add emojicons"
    )

    chat_completion = make_msg_from_prompt(job_description, prompt)
    return chat_completion.choices[0].message.content


def compare_with_resume(job_description: str, resume: str):
    prompt = (
        "Compare user's Resume with Job Description and give all the insights if he is eligible for the job or not."
        "use emojicons like ticks and cross"
        f"Resume: {resume}"
    )

    chat_completion = make_msg_from_prompt(job_description, prompt)
    return chat_completion.choices[0].message.content


def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()  # unique dir
    # clone repo in temp dir
    git.Repo.clone_from(repo_url, temp_dir)
    return temp_dir


def read_repo_files(repo_path, max_files=50):
    code_files = []
    supported_files = ('.py', '.js', '.ts', '.java', '.cpp', '.md', '.json', '.html', '.css')
    ignore_dirs = [".git", "venv", "env", ".env", "node_modules", "__pycache__", ".devcontainer",
                   ".idea", ".vscode", ".github", "dist", "build", "out", "target", ".next", ".turbo",
                   ".pytest_cache", ".mypy_cache", ".tox", ".cache", "logs", ".DS_Store",
                   "__snapshots__", ".coverage", ".parcel-cache", ".scannerwork"]

    for root, dirs, files in os.walk(repo_path):
        if any(skip in root for skip in ignore_dirs):
            continue

        for file in files:
            if file.endswith(supported_files):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        code = f.read()
                        code_files.append((full_path, code))
                        if len(code_files) >= max_files:
                            return code_files
                except Exception:
                    continue
    return code_files


def summarize_with_groq(code_files):
    summaries = []
    # summarize each file separately
    for path, code in code_files:
        prompt = f"""
        You are a senior software engineer and expert code reviewer.

        Below is the content of a single file from a GitHub project:

        --- BEGIN FILE ---
        {code[:3000]}
        --- END FILE ---

        Please provide a clear and concise summary of what this file does.

        - Use bullet points if helpful
        - Include relevant emojis to make it more engaging (e.g., 🧠, ⚙️, 🔍, ✅)
        - Keep the explanation developer-friendly and easy to scan
        """
        messages = [{"role": "user", "content": prompt}]

        chat_completion = call_groq(messages)
        summary = chat_completion.choices[0].message.content
        summaries.append(f"🔹 **{os.path.basename(path)}**\n{summary}")
    return "\n\n".join(summaries)


def summarize_github_repo(github_repo_link):
    try:
        repo_path = clone_repo(github_repo_link)
        code_files = read_repo_files(repo_path)
        if not code_files:
            return "No readable code files found."
        return summarize_with_groq(code_files)
    except Exception as e:
        return f"❌ Error while summarizing: {str(e)}"


def generate_linkedin_post(repoSummary):
    # repoSummary = summarize_github_repo(github_repo_link)
    prompt = f"""
        You are an experienced software engineer and a strong technical communicator.

        Below is a high-level summary of the repository’s contents, including an overview of each file:
        {repoSummary}

        Using this context, write a concise and engaging LinkedIn post that highlights:
        - What the project is and what it does
        - Why it's useful or interesting
        - Any key technical highlights or unique aspects
        - A call to action or invitation to check it out
        - What all have i learned making this project

        Keep the tone professional yet approachable, suitable for a LinkedIn audience of developers and tech professionals.
        No preamble.
    """
    messages = [{"role": "user", "content": prompt}]
    response = call_groq(messages)
    linkedin_post = response.choices[0].message.content.strip()

    return linkedin_post
