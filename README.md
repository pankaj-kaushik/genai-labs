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
│   │   ├── app.py
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
