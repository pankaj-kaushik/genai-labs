# 🤖 AI Email Writer Using Gemini and Python

## 🚀 Introduction
**An AI-powered Email and Message Writer** is a beginner-friendly Generative AI project that demonstrates how Large Language Models (LLMs) can generate professional emails using structured prompts. This project focuses on **prompt engineering fundamentals**, showing how role instructions, tone control, and prompt templates can significantly improve output quality.


## ✨ What This Project Does
This tool generates professional, well-structured emails based on user inputs such as:
- 🎯 Purpose of the email
- 🗣️ Desired tone (formal, friendly, persuasive, apologetic, etc.)
- 👤 Recipient type (client, manager, HR, customer)
- 📝 Message summary

Using these inputs, the system dynamically builds a prompt and sends it to the Gemini LLM to produce a ready-to-use email.

## 🎯 Learning Outcomes
After completing this project, you will understand
- How to integrate Gemini LLM APIs using Python
- How to design **structured prompt templates**
- How **role prompting** influences LLM behavior
- How to dynamically inject variables into prompts
- How to build simple **AI-powered productivity tools**

## 🧩 Use Cases
- 📩 Customer support email drafting
- 👔 HR communication automation
- 📢 Sales outreach personalization
- 🧾 Internal business communication generation
- 📬 Follow-up and reminder emails
- 👔 Productivity automation

## 🧩 Architecture & Sequence Flow
```text
User -> CLI/Web Interface -> User Inputs(purpose, tone, receipient, key points ) -> Prompt Builder -> Gemini LLM API -> Response Processor -> Formatted Output to User
```
1. User provide email inputs - purpose, tone, recipient, key points
2. Application build structured prompt using user inputs
3. Prompt is sent to Gemini LLM API
4. Gemini analyzes prompt and generates email template
5. Application processes and formats response
6. Output displayed to user

## ▶️ How to Run the Project
### Run Application
```bash
python gemini-email-writer.py
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
- Multi-language Email Generation
- Email Tone Analyzer (classify tone before sending)
- CRM Integration (HubSpot / Zoho / Salesforce)
- Chat-style conversation 
- Add Streamlit web UI
- Save generated emails/message to file (text/pdf)
- Auto reply generator


## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community