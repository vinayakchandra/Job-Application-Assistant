# 🚀 Job Application Assistant

Transform any job description into a personalized cover letter—along with a strategy to stand out and secure the role.
Built with the lightning-fast `Llama-4` model from `Groq` and a sleek `Streamlit` interface.

## ✨ Features

| Tab                  | What it does                                                                                              |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| **📄 Cover Letter**  | Crafts a concise, professional cover letter and suggests links (résumé, portfolio, GitHub, LinkedIn).     |
| **💡 Project Ideas** | Brainstorms portfolio projects to showcase the exact skills the role requires.                            |
| **🔍 Job Insights**  | Extracts key responsibilities, must-have skills, and hiring-manager priorities.                           |
| **🖥️ Tech Stack**   | Lists all technologies and tools mentioned in the posting, sprinkled with emojis for at-a-glance reading. |

## 🏁 Quick Start

```bash
pip install -r requirements.txt
# Add your GROQ key
echo "GROQ_API_KEY=sk-••••••" > .env
# Launch
streamlit run app.py
```

