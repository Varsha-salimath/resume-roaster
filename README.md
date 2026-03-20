# 🔥 Resume Roaster

> **We roast it so recruiters don't have to.**

An AI-powered resume analyzer that gives you brutally honest feedback AND rewrites your resume — all in one click.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ What It Does

Upload your PDF resume and get two things instantly:

| 🔥 The Roast | ✨ The Rewrite |
|---|---|
| Brutally honest, funny feedback | ATS-optimized, stronger version |
| Flags weak action verbs | Adds quantified achievements |
| Spots ATS red flags | Professional tone & structure |
| Points out missing metrics | Ready to send to recruiters |

---

## 🚀 Live Demo

👉 **[Try it here → resume-roaster2.streamlit.app](https://resume-roaster2.streamlit.app)**

---

## 🛠️ Tech Stack

- **Frontend & Backend** — Streamlit
- **AI Engine** — Google Gemini 2.0 Flash
- **PDF Parsing** — pdfplumber
- **PDF Export** — ReportLab
- **Deployment** — Streamlit Cloud

---

## 📦 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Varsha-salimath/resume-roaster.git
cd resume-roaster

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Run the app
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free API key at [aistudio.google.com](https://aistudio.google.com)

---

## 📁 Project Structure

```
resume-roaster/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and secrets
└── .streamlit/
    └── config.toml     # Streamlit theme config
```

---

## 🎯 How It Works

1. 📄 Upload your PDF resume
2. 🤖 Gemini AI analyzes it with two specialized prompts
3. 🔥 **Roast panel** — shows every weakness, vague bullet, and ATS problem
4. ✨ **Rewrite panel** — shows the improved, recruiter-ready version
5. 💾 Download the rewritten resume as PDF

---

## 🙋‍♀️ Built By

**Varsha Salimath** — M.Tech CSE Student & EdTech Developer

[![GitHub](https://img.shields.io/badge/GitHub-Varsha--salimath-black?style=flat&logo=github)](https://github.com/Varsha-salimath)

---

⭐ **If this helped you land a job, drop a star!**
