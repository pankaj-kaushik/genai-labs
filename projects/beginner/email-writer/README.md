# 🤖 AI Email / Message Writer (Gemini LLM)

An AI-powered Email and Message Writing Assistant built using **Python** and **Google Gemini LLM**.  
This tool helps users generate professional, friendly, or persuasive emails/messages instantly based on purpose, tone, and key points.


This project helps learners quickly create email/message without any expertise.

This project is ideal for:
- Students 📚
- Marketing professionals 👨‍💻
- Content creators ✍️
- Anyone who wants to create message quickly

## 🚀 What This Project Does
- Generate professional emails/messages using AI
- Control tone (Formal, Friendly, Persuasive, etc.)
- Supports different recipient types (Client, Boss, Friend, etc.)
- CLI-based interface
- Modular and scalable architecture
- Easy to extend with new AI capabilities

## 🎯 Learning Outcomes
- How GenAI APIs work
- Prompt Engineering Basics
- Secure API key handling
- Real-world GenAI use cases
- End-to-end AI application flow

## 🧩 Use Cases
- Writing professional emails
- Client communication drafts
- Follow-up messages
- Apology / Request emails
- Personal or casual message generation
- Productivity automation

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd email-writer
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
⚠️ Never commit .env to GitHub.

## ▶️ How to Run the Project
### Run main.py
```bash
python main.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
In `create_email_prompt()` method we passed the instruction in `user_prompt` (see below) but didn't mention any specific examples. The code tells the AI **what** to do (write an email) and **how** to format it (Subject/Body), but it gives zero finished examples of a "good" email for the AI to copy. It relies entirely on the AI's pre-existing knowledge of what a professional email looks like.


### Structured Prompting
In `create_email_prompt()` method we passed the instruction in `user_prompt` (see below) that dictate the organization of the input and the exact layout of the output.
Instead of writing a long, conversational sentence, we used **labels** and **delimiters** to organize the information.

- **Input Structuring:** Using headers like KEY POINTS TO INCLUDE: helps the AI distinguish between the "context" (who the email is for) and the "content" (what must be said).

- **Output Structuring:** The RESPONSE FORMAT: section forces the AI to follow a specific pattern (SUBJECT: followed by BODY:), making it "machine-readable" so you could easily split the text later using Python.

```python
user_prompt = f"""
    Write a {tone} email/message to {recipient} regarding '{purpose}'.
    Key points to include: 
    {key_points}.
    
    RESPONSE FORMAT:
    Please provide the response in the following format:
    Subject: [Subject Line]
    Body: [Email Body]

    Guidelines
    - Keep language natural and human-like
    - Maintain clarity and professionalism
    - Add proper greeting and closing
    - Keep it concise but complete
    Generate only the final email/message.
```
### Role Prompting
In `generate_email()` method, we passed the `system_instruction` parameter in the configuration which ensures the AI stays in **specialist** mode or role regardless of the query.
Instead of just asking for an email, we are explicitly telling the AI to act as a specific professional (a "helpful assistant"). This sets the "mental" framework for the AI, influencing its vocabulary, level of formality, and overall perspective before it even looks at your specific email details.

```python
system_instructions = "You are a helpful assistant that writes emails and messages."
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            config=genai.types.GenerateContentConfig(system_instruction=system_instructions),
            contents=prompt
        )

```
## 📌 Sample Output
```powershell
--- Welcome to your AI Email & Message Writer! ---
Please provide details for the email/message you want to create.
Enter purpose of the email or message: Project Update 
Enter desired tone (e.g., formal, casual, enthusiastic): formal
Enter recipient details (e.g., friend, colleague, client): client
Enter key points to include (separated by commas): Q3 launch is delayed by 2 weeks due to server migration issues. Will let you know updated date by tomorrow eod
Creating Email Prompt...
Creating Gen AI client...
Generating email/message... Please wait.

--- Generated Email/Message ---
Subject: Project Update: Q3 Launch Schedule

Body:
Dear [Client Name],

I am writing to provide an update regarding our upcoming Q3 launch.

Due to some unexpected technical challenges encountered during the server migration process, we have had to adjust our timeline. As a result, the launch will be delayed by approximately two weeks.

Our team is working to finalize the revised schedule, and I will follow up with a confirmed launch date by the end of the day tomorrow.

Thank you for your patience and understanding as we work to ensure a smooth transition.

Best regards,

[Your Name]
[Your Title]
------------------------------
```
## ✨ Future Enhancements
- Difficulty level selection (Beginner/Intermediate/Advanced)
- Hindi/Multi-language explanation support
- Chat-style conversation 
- Add Streamlit web UI
- Save generated emails/message to file (text/pdf)
- Auto reply generator


## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community