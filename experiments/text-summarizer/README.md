# 🧠 AI Text Summarizer (Using Gemini LLM)

A beginner-friendly **GenAI project built with Python** that summarizes long text into short, easy-to-understand bullet points using **Google Gemini Large Language Model**.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from long articles

## 🚀 What This Project Does
- Takes **long text input** from the user
- Sends it to **Gemini LLM**
- Returns a **concise summary** in simple language
- Uses **bullet points** for better readability

## 🎯 Learning Outcomes
- How GenAI APIs work
- Prompt engineering basics
- Secure API key handling
- Real-world GenAI use cases
- End-to-end AI application flow 

## 🧩 Use Cases
- Summarizing blog posts or articles  
- Making quick notes from study material  
- Understanding long documentation faster  
- Preparing revision notes  

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd text-summarizer
```
### Step 2: Create Virtual Environment
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
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Get Gemini API Key
- Visit Google AI Studio (https://aistudio.google.com/api-keys)
- Create a new API Key
- Copy the key

### Step 5: Create .env File
- Create a file named ```.env``` in the root directory and update the Gemini API Key
- Note: You can use ```.env.example``` file and rename it to ```.env```
- ⚠️ Never commit .env to GitHub.

## ▶️ How to Run the Project
### Step 1: Update ```input.txt``` File
Copy and past content of your blog post or article in input.txt file
### Step 2: Run main.py
```bash
python main.py
```
## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
In the `basic_summary()` method, the instruction **"Summarize this in one line"** is passed directly to the model without additional context or examples. This approach relies entirely on the model's pre-trained knowledge of effective summarization, providing minimal guidance on both the desired format and quality standards.

```python
response = client.models.generate_content(
            model=TARGET_MODEL, contents=f"Summarize this in one line : {content}"
        )
```

### Role Prompting
In the `professional_summary()` method, we provided a persona as part of the prompt to guide the model's behavior. By instructing the AI to act as a professional editor, we established a contextual framework that influences its vocabulary, level of formality, and overall approach to processing the input text.

Prompt Used
```text
You are a professional editor. Summarize the following text in simple language.\nUse 4-5 bullet points.\nMake it easy for beginners to understand.
```

```python
response = client.models.generate_content(
            model=TARGET_MODEL,
            contents=f"{user_prompt}"
        )
```

## 📌 Sample Output
```powershell
--- Welcome to your Text Summarizer Writer! ---
Reading input text from file...
Prompt Used...
You are a professional editor. Summarize the following text in simple language.
Use 4-5 bullet points.
Make it easy for beginners to understand.

Creating Gen AI client...
Generating Basic summary...
Basic Summary:
 AI is a transformative technology with diverse applications that offers significant potential while requiring ethical oversight and public literacy for responsible development.
Generating Professional summary...
Professional Summary:
 Here is a simple summary of the text:

*   **What it is:** Artificial Intelligence (AI) refers to computer systems that can perform tasks usually done by humans, such as learning from information and solving problems.     
*   **How we use it:** AI is already everywhere, helping doctors find diseases, allowing banks to stop fraud, and powering tools like self-driving cars and virtual assistants.        
*   **The risks:** While helpful, AI raises concerns about privacy, unfairness (bias), and the possibility of replacing human jobs.
*   **The future:** New technology will make AI even more powerful, but researchers are working to ensure humans can still understand and control how it makes decisions.
*   **Why it matters:** As AI becomes a bigger part of our lives, it is important for everyone to learn how it works so we can use it safely and responsibly.
```
## ✨ Future Enhancements
- Add Streamlit web UI
- Support PDF / text file input
- Choose summary length (short / medium / detailed)
- Add summary styles
  - Bullet Points
  - Executive Summary
  - One Line Summary
- Language selection (English / Hindi)
- Save summaries to file

## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community