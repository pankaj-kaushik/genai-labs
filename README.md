# 🧪 GenAI Labs

**GenAI Labs** is a personal experimentation playground for learning and exploring **Generative AI use cases** using Python and modern LLMs.

This repository contains **small, focused GenAI experiments**, each living in its own folder, designed to:
- understand LLM fundamentals
- learn prompt engineering
- explore real-world GenAI use cases
- build intuition before production-grade systems

> ⚠️ This repo is **not production-ready**. The goal is learning by building.

---

## 📂 Repository Structure

```text
genai-labs/
│
├── experiments/
│   ├── text-summarizer/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   ├── chat-with-pdf/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   └── ...
│
├── .env.example
├── .gitignore
└── README.md
```

**Each experiment:**
- is self-contained
- has its own dependencies
- can be run independently

---

## 🧠 What You’ll Learn from This Repo

By going through these experiments, you will learn:

- How LLMs work at a practical level
- Prompt design & prompt tuning
- Using LLM APIs (Gemini / OpenAI / others)
- Handling tokens, temperature, max output
- Building GenAI pipelines (input → LLM → output)
- Using embeddings & vector search (in later labs)
- Structuring GenAI projects properly

**Perfect for:**

- Beginners in GenAI
- Software engineers exploring AI
- System design + GenAI learners

---
## 🛠 Tech Stack
Common stack used across experiments:
- **Language:** Python 3.10+
- **LLMs:** Google Gemini
- **Frameworks:** langchain
- **Env Management:** python-dotenv
- **IDE:** VS Code (recommended)

**📌 Each experiment may use additional libraries — check its requirements.txt**

---
## ⚙️ Environment Setup (One-Time)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/genai-labs.git
cd genai-labs
```
### Step 2: Create a Virtual Environment
```bash
python -m venv .venv
```
Activate it:

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```
### Step 3: Setup Environment Variables
Create a .env file at the root
```text
GEMINI_API_KEY="your_api_key_here"
OPENAI_API_KEY="your_api_key_here"
```
👉 Refer to ```text.env.example```
👉 **Never commit** ```text.env``` **to GitHub**

---
## ▶️ How to Run Experiments
Each experiment follows the same basic flow.

### Step 1: Move into the experiment folder
```bash
cd experiments/<experiment-name>
```
### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Run the project
```bash
python main.py
```
**📌 Always check the experiment’s README for exact commands.**

---
## 🧪 How to Add a New Experiment
Follow this standard structure:
```text
experiments/
└── new-experiment-name/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── assets/ (optional)
```
Best practices:
- Focus on one GenAI concept
- Keep code minimal & readable
- Document:
  - what the experiment does
  - what you will learn
  - how to run it

---
## 🧭 Planned / Example Experiments
Some experiments you may find or add
- Study Buddy / Concept Explainer
- Email / Message Writer
- Chat with PDF
- Resume Analyzer
- Prompt Comparison Lab
- Embeddings Search Demo
- RAG (Retrieval Augmented Generation)
- Simple AI Agent
- Interview Question Generator
- Career Coach For S/W Engineers
- Bug Root Cause Analyzer
- Teacher for kids (Math/Logic)

---
## 🚀 Who Should Use This Repo?
- 👨‍💻 Software engineers exploring GenAI
- 🎓 Beginners learning LLMs
- 🧠 System designers adding AI to systems
- 📚 Anyone who prefers learning by building
---
## ⚠️ Disclaimer
- LLM APIs may incur cost
- Outputs may vary due to model randomness
- This repo is for learning & experimentation only

---
## ⭐ Support

If you find this repository useful:
- Star ⭐ the repo
- Fork it
- Modify experiments
- Build your own labs

**Happy experimenting 🧪🚀**