# 🤖 AI Resume Analyzer (Gemini LLM)

AI Resume Analyzer is an **intelligent** Python-based application that uses Large Language Models (LLMs) to analyze resumes and provide actionable insights for improving resume quality, clarity, and job readiness. 


The system evaluates resumes for structure, skills, relevance, and optimization, helping candidates present their profiles more effectively.

This project is ideal for:
- 🎓 Students preparing for internships and job placements
- 💼 Professionals improving their resumes for career transitions
- 👨‍💻 Developers learning Generative AI application development
- 🏢 Recruiters or career platforms building automated resume screening tools
- 🌍 Anyone interested in applying LLM APIs to real-world productivity tools

## 🚀 What This Project Does
The AI Resume Analyzer performs automated resume evaluation and generates:

- 📊 Resume quality analysis  
- 🧠 Skill extraction and gap identification  
- ✨ Resume improvement suggestions  
- 📄 ATS (Applicant Tracking System) optimization recommendations  
- ✍️ Resume rewriting suggestions for better clarity and professionalism

## 🎯 Learning Outcomes
By building or using this project, you will learn:

- 🔌 How to integrate LLM APIs into Python applications  
- 🧩 Prompt engineering for structured AI outputs  
- 📑 Resume parsing and document processing  
- 🏗️ Building real-world AI productivity tools  
- 🧱 Designing modular AI application architecture  
- 🔄 Handling PDF input and text extraction workflows

## 🧩 Use Cases
- 📌 Resume improvement before job applications  
- 📈 Skill gap analysis for career planning  
- 🧑‍🏫 Career coaching tools and HR platforms  
- 📚 Educational projects for learning LLM integrations  
- 🏫 Automated resume feedback systems for placement cells  
- 🏢 Internal employee resume optimization tools

## 🧩 Architecture & Sequence Flow
```text
User -> CLI/Web Interface -> Resume Reader (PDF/Text Parser) -> Prompt Builder -> Gemini LLM API -> Response Processor -> Formatted Output to User
```
1. User uploads resume (pdf/text)
2. Application extract text from resume
3. System builds a structured prompt
4. Prompt is sent to Gemini LLM API
5. Gemini analyzes resume and generates response
6. Application processes and formats response
7. Improved resume + suggestion displayed to user

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd resume-analyzer
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

### Step 1: Replace ```resume.pdf``` under ```data``` directory.
Copy and past your resume in pdf format with file name ```resume.pdf``` under ```data``` directory

### Step 2: Run main.py
```bash
python main.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Role Prompting
In `create_user_prompt()` method we passed the instruction in `user_prompt` (see below) but didn't mention any specific examples. The code tells the AI **what** to do (Improve the following resume professionaly.) and **instructions** to generate required information, but it gives zero finished examples of a "good" rfor the AI to copy. It relies entirely on the AI's pre-existing knowledge of what a good explanation looks like.


### Structured Prompting
In `create_user_prompt()` method we passed the instruction in `user_prompt` (see below) that dictates the organization of the input and the exact layout of the output. We provided explicit structured instructions with numbered items (1, 2, 3) to ensure the AI generates organized, multi-faceted output covering key strengths, improvement areas, and ATS compatibility. We used clear section headers like ```Resume content:``` to separate instructions from the actual resume data. We also applied **context injection** by dynamically embedding the resume content into the prompt template.

```python
user_prompt = f"""
 user_prompt = f"""

        Improve the following resume professionaly.
        Also provide:
        1. Key strengths and skills highlighted in the resume.
        2. Areas for improvement in terms of content, structure, and formatting.
        3. ATS (Applicant Tracking System) compatibility analysis and suggestions.

        Resume content:
        {content}
        """
```
### Role Prompting
In `analyze_resume()` method, we passed the `system_instruction` parameter via `GenerateContentConfig` to enforce a consistent professional role. The instruction "You are an expert resume writing assistant. Please analyze the following resume:" explicitly defines the AI's identity and expertise domain. This role definition acts as a persistent behavioral anchor throughout the interaction, shaping the AI's tone, vocabulary, technical depth, and analytical approach—ensuring it responds as a specialized professional rather than a general-purpose assistant. We also configure the `temperature` parameter for consistent output quality.

```python
  system_instructions = "You are an expert resume writing assistant. Please analyze the following resume:"
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instructions,
                temperature=TEMPERATURE
            ),
            contents=prompt
        )
```
## 📌 Sample Output
```powershell
--- Welcome to your AI Resume Analyzer! ---
Analyzing code from file: data/resume.pdf
Creating Gen AI client...
Explaining resume... Please wait.

------------------------------------------------------------
This is a solid foundation for a Python Developer resume. You have quantifiable metrics (percentages and hours saved), wh
look for.

Below is the professionally improved version of your resume, followed by the requested analysis.

---

# IMPROVED RESUME: ALEX R. DEVELOPER

**ALEX R. DEVELOPER**
New York, NY | (555) 012-3456 | alex.dev@email.com
[linkedin.com/in/alexdev](https://linkedin.com/in/alexdev) | [github.com/alexdev](https://github.com/alexdev)

**PROFESSIONAL SUMMARY**
Performance-driven Python Developer with over 2 years of experience designing scalable backend architectures and automatengo, FastAPI, and Flask with a focus on writing PEP 8-compliant, maintainable code. Proven track record of optimizing sysd streamlining CI/CD workflows using Docker and AWS.

**TECHNICAL SKILLS**
*   **Languages:** Python (Advanced), SQL (PostgreSQL, MySQL), JavaScript (ES6+), HTML5/CSS3.
*   **Frameworks:** Django, FastAPI, Flask, Django REST Framework (DRF), Celery.
*   **DevOps & Tools:** Docker, AWS (EC2, S3, RDS), Jenkins, Nginx, Git, Redis, RabbitMQ.
*   **Testing & Quality:** PyTest, Unittest, Mock, CI/CD, PEP 8.
*   **Libraries:** Pandas, NumPy, BeautifulSoup, Selenium, SQLAlchemy.

**PROFESSIONAL EXPERIENCE**

**TechStream Solutions** | New York, NY
*Junior Python Developer* | Jan 2024 – Present

*   **API Development:** Architected and deployed 10+ RESTful APIs using FastAPI and DRF, reducing frontend-backend laten
programming.
*   **Performance Optimization:** Refactored legacy data processing scripts, achieving a 40% increase in execution speed 
*   **Infrastructure & DevOps:** Collaborated with DevOps to containerize microservices using Docker, reducing deployment CI/CD pipeline.
*   **Database Management:** Optimized complex PostgreSQL queries and implemented Redis caching, maintaining sub-second ric periods (50k+ concurrent users).

**Innovate AI** | New York, NY
*Associate Developer* | June 2022 – Dec 2023

*   **Process Automation:** Developed an automated financial reporting tool using Pandas and Openpyxl, eliminating 10 man
the accounting department.
*   **Application Maintenance:** Managed and debugged a high-traffic Flask application, resolving 50+ high-priority techn system stability by 20%.
*   **Cloud Migration:** Facilitated a seamless migration of 2TB of on-premise data to AWS S3 and RDS, ensuring 100% dataer recovery capabilities.

**KEY PROJECTS**

**Real-Time Task Orchestrator** | *Python, Celery, RabbitMQ, WebSockets*
*   Engineered a distributed task queue system capable of handling 1,000+ concurrent background jobs.
*   Integrated a real-time monitoring dashboard using WebSockets to provide live status updates to users.

**E-Commerce Price Intelligence Tool** | *Python, Selenium, SMTP, AWS*
*   Developed a scalable web scraper to track price fluctuations across 5+ major retail platforms.
*   Built an automated notification engine that delivers real-time email alerts to 500+ subscribers based on price-drop t

**EDUCATION**

**Bachelor of Science in Computer Science**
State University of Technology | Graduated 2022

**CERTIFICATIONS**
*   **PCAP:** Certified Associate in Python Programming
*   **AWS Certified Cloud Practitioner**

---

### 1. Key Strengths & Skills Highlighted
*   **Quantifiable Impact:** You successfully used metrics (40% speed increase, 10 hours saved). This moves the resume frriented."
*   **Modern Tech Stack:** Inclusion of FastAPI and Celery shows you are current with modern Python trends (asynchronous ks).
*   **Cloud & DevOps Knowledge:** Showing familiarity with AWS, Docker, and Jenkins is a massive plus for a developer, asull lifecycle of an application.
*   **Strong Foundation:** A BS in Computer Science combined with industry-standard certifications (PCAP, AWS) validates 
knowledge.

### 2. Areas for Improvement
*   **Summary Specificity:** The original summary was a bit generic. I updated it to include "backend architecture" and "ywords.
*   **Action Verbs:** I replaced passive words like "assisted" or "built" with stronger verbs like "Architected," "Engineinated."
*   **Project Context:** In the original, the projects were a bit thin. I added a "Tech Stack" line to each project so re*   **Action Verbs:** I replaced passive words like "assisted" or "built" with stronger verbs like "Architected," "Engineinated."
*   **Project Context:** In the original, the projects were a bit thin. I added a "Tech Stack" line to each project so reinated."
*   **Project Context:** In the original, the projects were a bit thin. I added a "Tech Stack" line to each project so re*   **Project Context:** In the original, the projects were a bit thin. I added a "Tech Stack" line to each project so re tools you used.
*   **Technical Depth:** I added specific libraries (DRF, SQLAlchemy, NumPy) to the skills section to ensure you hit more

### 3. ATS (Applicant Tracking System) Analysis & Suggestions
*   **Analysis:** Your resume is highly ATS-friendly because it uses a standard layout, clear headings, and avoids comple
*   **Keyword Optimization:** You have a good density of keywords (Python, Django, AWS, Docker, RESTful APIs).
*   **Suggestions for the Future:**
*   **Analysis:** Your resume is highly ATS-friendly because it uses a standard layout, clear headings, and avoids comple
*   **Keyword Optimization:** You have a good density of keywords (Python, Django, AWS, Docker, RESTful APIs).
*   **Suggestions for the Future:**
*   **Keyword Optimization:** You have a good density of keywords (Python, Django, AWS, Docker, RESTful APIs).
*   **Suggestions for the Future:**
*   **Suggestions for the Future:**
 (not a scan of an image).
    *   **Standard Headers:** Stick to standard headers like "Professional Experience" and "Education" so the system knows exactly where to categorize your data.
    *   **Customization:** When applying for a specific job, look at their "Requirements" section. If they mention "Redshift" and you’ve used it, make sure that specific word is in your skills list.
 (not a scan of an image).
    *   **Standard Headers:** Stick to standard headers like "Professional Experience" and "Education" so the system knows exactly where to categorize your data.
    *   **Customization:** When applying for a specific job, look at their "Requirements" section. If they mention "Redshift" and you’ve used it, make sure that specific word is in your skills list.
------------------------------------------------------------
```
## ✨ Future Enhancements

- 📊 Job Description vs Resume matching score  
- 📉 Resume scoring dashboard with analytics  
- 🌐 Streamlit or web-based UI  
- 📥 Resume rewriting with downloadable PDF output  
- 📂 Batch resume analysis for recruiters  
- 🗄️ Vector database integration for role-based recommendations  
- 🌎 Multi-language resume support  
- 🛤️ AI-powered career roadmap suggestions


## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community