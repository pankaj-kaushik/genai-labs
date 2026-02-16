# ✉️ AI Email Writer Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Email Writer** - your intelligent assistant for crafting professional, personalized emails and messages!
This **beginner-friendly** project demonstrates how to leverage **Large Language Models (LLMs)** with **prompt engineering** techniques to automatically generate high-quality business communications.

Instead of spending time drafting emails from scratch, this system allows you to:

- 🎯 **Specify your purpose** and let AI write the perfect message
- 🗣️ **Control the tone** (formal, casual, enthusiastic, apologetic)
- 👤 **Target specific recipients** (clients, managers, HR, customers)
- 📝 **Include key points** automatically in a natural flow
- ⚡ **Generate instantly** saving time and mental effort
- 📧 **Get structured output** with subject line and body

Perfect for beginners learning AI integration, Prompt Engineering, and building practical productivity tools!

## 🚀 What This Project Does
- Collects user inputs through an interactive CLI interface
- Dynamically constructs structured prompts based on user specifications
- Generates professional, well-formatted emails using Gemini LLM
- Handles multiple email contexts (business, customer support, HR, sales)
- Provides error handling for robust API interactions
- Delivers ready-to-use emails with proper greeting and closing

The tool generates emails tailored to your specific needs:

### 🎯 Purpose-Driven Generation
- Define the **main objective** of your email
- AI understands context and intent
- Generates relevant, focused content
- Perfect for **project updates**, **meeting requests**, **follow-ups**

### 🗣️ Tone Customization
- **Formal**: Professional business communication
- **Casual**: Friendly, relaxed messaging
- **Enthusiastic**: Energetic, positive outreach
- **Apologetic**: Sincere, empathetic responses
- **Persuasive**: Compelling, action-oriented emails

### 👤 Recipient-Aware Messaging
- Adapts language to **audience type**
- Maintains appropriate **formality level**
- Uses context-specific **vocabulary**
- Ensures **professional etiquette**

### 📝 Key Points Integration
- Seamlessly incorporates your **main points**
- Organizes information **logically**
- Maintains **natural flow**
- Ensures **completeness**

## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🔌 How to integrate **Gemini LLM APIs** using Python
- 📝 How to design **structured prompt templates**
- 🎭 How **role prompting** influences LLM behavior
- 🔄 How to **dynamically inject variables** into prompts
- ⚠️ How to implement **comprehensive error handling**
- 🏗️ How to structure **modular, maintainable code**
- 🔐 How to manage **API keys** securely with environment variables
- 🧪 **Comparative prompt experimentation** techniques

This project strengthens both **AI integration** skills and **practical application development**.

## 🏢 Industry Use Cases
- 📩 **Customer Support**
  - Automated response drafting
  - Complaint resolution emails
  - FAQ response generation
  - Support ticket follow-ups

- 👔 **Human Resources**
  - Interview scheduling
  - Candidate communication
  - Employee announcements
  - Policy update notifications

- 📢 **Sales & Marketing**
  - Outreach personalization
  - Follow-up sequences
  - Proposal introductions
  - Client onboarding emails

- 💼 **Internal Communication**
  - Team updates
  - Meeting requests
  - Project status reports
  - Collaboration invitations

- 🔔 **Reminders & Follow-ups**
  - Payment reminders
  - Deadline notifications
  - Event confirmations
  - Task follow-ups

- 🎓 **Academic & Professional**
  - Networking messages
  - Reference requests
  - Application follow-ups
  - Thank you notes

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> Input Collection -> Prompt Builder -> Gemini LLM API -> Response Processor -> Formatted Email Output
```
Detailed Flow:\

1. Application starts - Welcome message displayed
2. User input collection - Interactive prompts gather:
- Purpose of the email
- Desired tone
- Recipient details
- Key points to include
3. Prompt construction - ```create_email_prompt()``` builds structured prompt
4. API client initialization - GenAI client created with authentication
5. Email generation - Prompt sent to Gemini with system instructions
6. Response processing - API response formatted and validated
7. Error handling - Graceful error management for robustness
8. Output display - Generated email shown with clear formatting

## ▶️ How to Run the Project
### Run Application
```python
python ai-email-writer.py
```
## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
The application uses zero-shot prompting - providing instructions without examples:

```python
email_prompt = f"""
Write a {tone} email/message to {recipient} regarding '{purpose}'.
Key points to include: {key_points}.
"""
```
**Why Zero-Shot?**
- Relies on model's pre-trained knowledge
- No need for example emails
- Flexible across different contexts
- Simpler prompt construction

### Structured Prompting
The prompt uses clear structure with labeled sections:
```python
RESPONSE FORMAT:
Please provide the response in the following format:
Subject: [Subject Line]
Body: [Email Body]
```

**Key characteristics:**
- Clear output format specification
- Labeled sections for parsing
- Explicit guidelines for content
- Machine-readable structure

### Role Prompting
System instructions set the AI's behavior and expertise.

```python
system_instructions = "You are a helpful assistant that writes emails and messages."
```
**Benefits:**
- Sets professional context
- Influences vocabulary and tone
- Maintains consistency
- Prevents off-topic responses

### Dynamic Variable Injection
User inputs are dynamically inserted into prompt templates:

```python
def create_email_prompt(purpose: str, tone: str, recipient: str, key_points: str) -> str:
    email_prompt = f"""
    Write a {tone} email/message to {recipient} regarding '{purpose}'.
    Key points to include: {key_points}.
    """
```
**Advantages:**
- Personalized email generation
- Reusable prompt template
- Maintainable code structure
- Easy to modify and extend

## 📌 Sample Output
```powershell
--- Welcome to your AI Email & Message Writer! ---
Please provide details for the email/message you want to create.
Enter purpose of the email or message: Project Update
Enter desired tone (e.g., formal, casual, enthusiastic): formal
Enter recipient details (e.g., friend, colleague, client): client
Enter key points to include (separated by commas): Q3 launch is delayed by 2 weeks due to server migration issues. Will let you know updated date by tomorrow eod
Creating Email Prompt...
Generating email/message... Please wait.

--- Generated Email/Message ---
Subject: Project Update: Q3 Launch Schedule

Body:
Dear [Client Name],

I am writing to provide an update regarding our upcoming Q3 launch.

Due to some unexpected technical challenges encountered during the server migration process, 
we have had to adjust our timeline. As a result, the launch will be delayed by approximately 
two weeks.

Our team is working to finalize the revised schedule, and I will follow up with a confirmed 
launch date by the end of the day tomorrow.

Thank you for your patience and understanding as we work to ensure a smooth transition.

Best regards,

[Your Name]
[Your Title]
------------------------------
```
## ✨ Future Enhancements
- 🌐 Multi-Language Support
  - Generate emails in multiple languages
  - Automatic translation
  - Locale-specific formatting
  - Cultural tone adaptation
- 📊 Email Tone Analyzer
  - Analyze tone before sending
  - Sentiment classification
  - Formality scoring
  - Suggestion improvements
- 🔗 CRM Integration
  - HubSpot connector
  - Salesforce integration
  - Zoho CRM sync
  - Auto-populate recipient data
- 💬 Conversational Interface
  - Chat-style interaction
  - Multi-turn refinement
  - Iterative editing
  - Context preservation
- 🌐 Web UI with Streamlit
  - Visual interface
  - Real-time preview
  - Template library
  - Copy-to-clipboard feature
- 💾 Output Management
  - Save to text/PDF files
  - Email history tracking
  - Template favorites
  - Export to email clients
- 🤖 Auto-Reply Generator
  - Analyze incoming emails
  - Generate contextual replies
  - Smart suggestions
  - Response templates
- 🎯 Template Library
  - Pre-built email templates
  - Industry-specific formats
  - Best practice examples
  - Customizable presets

## 🐛 Troubleshooting
Common Issues:

**API Key Error:**
```python
Error: GEMINI_API_KEY not found
Solution: Create .env file with your API key
```
**File Not Found:**
```python
Error: Could not find input file
Solution: Ensure sample_article.txt exists in the project directory
```
**Connection Error:**
```python
Error: Connection error while calling Gemini API
Solution: Check your internet connection and API status
```
**Timeout Error:**
```python
Error: Request timed out
Solution: Try again or check API service status
```

## 📝 Configuration Tips
Prompt Design Guidelines:
- **Be specific:** Clearly state the desired output format
- **Set constraints:** Define tone, length, and structure
- **Use action verbs:** "Write", "Generate", "Draft"
- **Test variations:** Experiment with different phrasings

Tone Selection Guidelines:

- **Formal:** Legal, executive, official communications
- **Casual:** Team messages, friendly outreach
- **Enthusiastic:** Marketing, sales, announcements
- **Apologetic:** Service issues, complaints, delays
- **Persuasive:** Sales pitches, proposals, requests

Model Selection:
- **gemini-3-flash-preview:** Fast, cost-effective for email generation
- Consider other models for specialized needs

## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your AI story platform

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community

---
Happy Email Writing! ✉️✨

Remember: Effective email generation starts with clear inputs and well-designed prompts. Experiment with different tones and purposes to discover what works best for your specific communication needs!
