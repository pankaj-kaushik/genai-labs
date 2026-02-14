# 🧠 AI Text Summarizer Using Gemini And Python

## 📌 Introduction
**AI-powered summarization** is a core capability used across research, legal, enterprise, and content platforms.
This **beginner-friendly** project demonstrates how **prompt engineering** techniques can significantly influence the quality, length, and structure of generated summaries using the Gemini LLM and Python.

## 🚀 What This Project Does
This application generates multiple summaries of the same article using different prompt styles:

- 📍 Bullet-point summary
- 📄 Executive summary
- ✨ One-line summary

It highlights how **prompt variations → output variations**, a foundational concept in real-world LLM systems.

## 🎯 Learning Outcomes
After completing this project, you will understand
- How to call LLM APIs using python
- How prompt design affects LLM outputs
- Zero-Shot style prompting
- Comparative prompt experimentation 

## 🏢 Industry Use Cases
- Research document summarization
- Legal and compliance review
- News aggregation systems
- Enterprise knowledge-base summarization
- Meeting transcript summarization 

## 🧩 Architecture & Sequence Flow
```text
User -> CLI/Web Interface -> Document Reader (PDF/Text Parser) -> Prompt Builder -> Gemini LLM API -> Response Processor -> Formatted Output to User
```
1. User uploads document (pdf/text)
2. Application extract text from document
3. System builds a structured prompt
4. Prompt is sent to Gemini LLM API
5. Gemini analyzes prompt and generates response
6. Application processes and formats response
7. Output displayed to user

## ▶️ How to Run the Project
### Step 1: Update ```sample_article.txt``` File
Copy and paste content of your article in ```sample_article.txt``` file

### Step 2: Run Application
```bash
python gemini-text-summarizer.py
```
## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
In the `prompts.py` file, we have specified different prompt instruction that is passed directly to the model without additional context or examples. This approach relies entirely on the model's pre-trained knowledge of effective summarization, providing minimal guidance on both the desired format and quality standards.

```python
BULLET_PROMPT = """
Summarize the following article into 5 bullet points:
"""
EXECUTIVE_PROMPT = """
Write a concise executive summary of the following article:
"""
ONE_LINE_PROMPT = """
Summarize the article in one single impactful sentence:
"""
```
## 📌 Sample Output
```powershell
--- Welcome to your AI Text Summarizer! ---
Reading input text from file...
Generating Basic summary...Please wait...

--- Bullet Point Summary ---
Here is a 5-point summary of the article:

*   **Definition and Technology:** Artificial Intelligence (AI) simulates human intelligence through machine learning and deep learning, using neural networks to process data and solve complex problems.
*   **Widespread Applications:** AI is utilized across various industries, including healthcare for diagnostics, finance for fraud detection, autonomous transportation, and natural language processing for virtual assistants.
*   **Ethical Considerations:** The development of AI raises significant concerns regarding data privacy, algorithmic bias, job displacement, and 
the need for transparent, accountable systems.
*   **Future Trends:** Ongoing advancements in quantum computing and neuromorphic chips are expected to enhance AI capabilities, while researchers work toward making AI more explainable and ensuring human oversight.
*   **Importance of Literacy:** As AI becomes more integrated into society, AI literacy is essential for individuals to understand the technology's limitations and make informed decisions about its regulation.

--- Executive Summary ---
**Executive Summary**

Artificial Intelligence (AI), driven by machine learning and deep learning, is transforming global industries by automating complex tasks and data analysis. While its applications offer significant benefits in healthcare, finance, and autonomous systems, the technology presents critical ethical challenges, including algorithmic bias, privacy risks, and workforce displacement. To ensure a beneficial future, development must prioritize 
transparency and "explainable AI," supported by a high level of societal AI literacy to guide responsible implementation and regulation.

--- One Line Summary ---
Artificial intelligence is a transformative force redefining human potential across every industry, requiring a critical balance between rapid technological innovation and the ethical accountability necessary to ensure a beneficial future for society.
```
## ✨ Future Enhancements
- Add Streamlit web UI
- Multi-document summarization
- Support PDF / URL ingestion pipeline
- Choose summary length (short / medium / detailed)
- Language selection (English / Hindi)
- Save summaries to file

## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀