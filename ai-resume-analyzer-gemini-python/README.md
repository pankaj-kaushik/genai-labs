# 📄 AI Resume Analyzer Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Resume Analyzer** - your intelligent assistant for optimizing resumes and boosting job application success! This **beginner-friendly** project demonstrates how to leverage **Large Language Models (LLMs)** with **prompt engineering** techniques to automatically analyze and improve resume quality.

Instead of manually reviewing and improving resumes, this system allows you to:

- 📊 **Get expert analysis** of resume strengths and weaknesses
- 🎯 **Identify skill gaps** and areas for improvement
- 📝 **Receive ATS optimization** suggestions for better screening results
- ✨ **Generate professional improvements** with actionable feedback
- 🔄 **Process multiple formats** (PDF and text files)
- 📈 **Boost job readiness** with data-driven recommendations

Perfect for beginners learning AI integration, Prompt Engineering, and building practical career development tools!

## 🚀 What This Project Does
- Reads resume content from PDF or text files automatically
- Extracts text from PDF documents using pypdf library
- Generates comprehensive resume analysis with structured feedback
- Demonstrates how **role-based prompting → expert-level analysis**
- Handles errors gracefully with comprehensive exception handling
- Provides a clean CLI interface for easy interaction
- Uses Google's Gemini LLM for professional resume evaluation

The tool generates three powerful analysis sections:

### 📊 Key Strengths Analysis
- Identifies **standout achievements** and metrics
- Highlights **relevant technical skills**
- Recognizes **quantifiable impact** statements
- Perfect for **understanding your competitive advantages**

### ⚠️ Improvement Areas
- Points out **weak language** and passive voice
- Suggests **stronger action verbs**
- Identifies **missing context** in experiences
- Recommends **technical depth** enhancements
- Great for **targeted resume refinement**

### 📈 ATS Compatibility Analysis
- Evaluates **keyword density** for applicant tracking systems
- Checks **formatting compatibility**
- Suggests **standard header usage**
- Provides **customization strategies** for specific jobs
- Perfect for **passing automated screening**

### ✨ Professional Resume Rewrite
- Generates **improved version** of your resume
- Implements **best practices** automatically
- Enhances **action-oriented language**
- Strengthens **technical descriptions**

## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🔌 How to integrate **Gemini LLM APIs** using Python
- 📝 How **role-based system instructions** influence AI behavior
- 🎯 How to implement **structured prompt design** for organized outputs
- 🔄 How to handle **PDF parsing** with pypdf library
- 📄 How to process **multi-format file input** (PDF and text)
- ⚠️ How to implement **robust error handling** for file operations
- 🏗️ How to structure **modular, maintainable code**
- 🔐 How to manage **API keys** securely with environment variables
- 🧪 **Context injection** techniques for dynamic prompts

This project strengthens both **AI integration** skills and **practical application development** best practices.

## 🏢 Industry Use Cases
- 📚 **Career Services & Education**
  - University placement cell automation
  - Student resume feedback systems
  - Career counseling tools
  - Job readiness assessment

- 💼 **Recruitment & HR**
  - Resume pre-screening assistance
  - Candidate feedback automation
  - Resume quality scoring
  - Internal employee development

- 🎯 **Career Coaching**
  - Professional resume review services
  - Client portfolio optimization
  - Job application strategy
  - Interview preparation support

- 📝 **Job Portals & Platforms**
  - Automated resume analysis features
  - Job-resume matching systems
  - Premium user services
  - Resume builder enhancements

- 🏢 **Corporate Training**
  - Employee upskilling programs
  - Internal mobility support
  - Resume writing workshops
  - Career development initiatives

- 🌐 **Freelance & Consulting**
  - Resume writing services
  - Career transition assistance
  - Professional branding
  - LinkedIn profile optimization

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> File Reader (PDF/Text Parser) -> Text Extraction -> Structured Prompt Builder -> Gemini LLM API (with Role Instructions) -> Response Processor -> Formatted Analysis + Improved Resume Display
```
**Detailed Flow:**

1. Application starts - User launches the CLI application
2. File type detection - System identifies PDF or text format
3. Content extraction - pypdf extracts text from PDF or reads text file
4. Prompt construction - Structured prompt with numbered requirements
5. API client initialization - Gemini client is created with API key
6. System instruction setup - Model is positioned as expert resume assistant
7. Content generation - Prompt is sent to Gemini API with temperature=1.0
8. Response processing - API response is formatted with sections
9. Error handling - Catches file, parsing, and API errors gracefully
10. Output display - Complete analysis with improved resume printed to console

## ▶️ How to Run the Project

### Step 1: Add Your Resume
Copy your resule file (pdf or text) under to ```data``` directory.
- For PDF: ```data/resume.pdf```
- For Text: ```data/resume.txt```

### Step 2: Update Target File
Modify the ```TARGET_FILE``` constant ```ai-resume-analyzer.py```.

```python
TARGET_FILE = "data/resume.pdf"  # or "data/resume.txt"
```

### Step 3: Run Application
```bash
python ai-resume-analyzer.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Role-Based System Instructions
The application uses system instructions to establish AI's expertise:

```python
system_instructions = "You are an expert resume writing assistant. Please analyze the following resume:"
```
**Why Role-Based Prompting?**
- Positions AI as a domain expert (resume writing)
- Ensures professional tone and vocabulary
- Improves analysis depth and quality
- Provides consistent perspective across analyses
- Activates relevant knowledge domains in the model

### Structured Prompting with Numbered Requirements
The prompt includes explicit numbered sections for organized output:
```python
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
**Key characteristics:**
- Numbered items (1, 2, 3) ensure organized, multi-faceted output
- Clear section headers separate instructions from data
- Explicit deliverables prevent incomplete responses
- Comprehensive coverage of analysis dimensions

### Context Injection Pattern
Dynamically embeds resume content into prompt template:

```python
f"""Resume content:
{content}
"""
```
**Benefits:**
- Separates structure from data for reusability
- Clear data boundaries with section headers
- Dynamic content insertion without hardcoding
- Maintainable prompt templates

### Task-Specific Prompt Design
The prompt is optimized for resume analysis:
```python
"Improve the following resume professionaly."
```
**Key characteristics:**
- Action-oriented verb ("Improve", "Analyze")
- Professional context specification
- Multiple analysis dimensions
- Specific domain focus (ATS, structure, content)

### Temperature Control for Creativity
Uses higher temperature (1.0) for creative improvements:
```python
TEMPERATURE = 1
```
**Benefits:**
- More creative rewording and suggestions
- Diverse phrasings for improvements
- Natural language variations
- Balanced between creativity and coherence

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

- 🌐 Web Interface with Streamlit
  - Drag-and-drop file upload
  - Real-time analysis display
  - Side-by-side comparison view
  - Export improved resume to PDF/DOCX
- 📊 Advanced Analytics
  - Resume scoring dashboard (0-100 scale)
  - Skill gap visualization
  - Industry benchmark comparisons
  - Keyword density heatmaps
- 🎯 Job Matching Features
  - Job description vs resume matching score
  - Role-based recommendations
  - Skill requirement alignment
  - Custom optimization for specific jobs
- 📄 Multi-Format Support
  - DOCX file parsing
  - Google Docs integration
  - LinkedIn profile import
  - HTML resume parsing
- 🔄 Batch Processing
  - Multiple resume analysis
  - Recruiter bulk screening tools
  - Team resume optimization
  - Portfolio management
- 💾 Output Management
  - Save analysis reports to files
  - Generate PDF reports with formatting
  - Export improved resumes
  - History tracking and comparison
- 🌍 Multi-Language Support
  - Resume analysis in multiple languages
  - Cross-cultural formatting tips
  - International resume standards
  - Localized best practices
- 🎓 Career Development Tools
  - AI-powered career roadmap suggestions
  - Skill development recommendations
  - Course and certification suggestions
  - Industry trend analysis
- 🔐 Enterprise Features
  - User authentication and profiles
  - Team collaboration tools
  - Usage analytics and tracking
  - API rate limiting
  - Cost monitoring per analysis
- 🤖 Advanced AI Features
  - Multiple resume format generation
  - Cover letter generation
  - LinkedIn profile optimization
  - Interview preparation tips
  - Salary negotiation insights

## 🐛 Troubleshooting
Common Issues:

**API Key Error:**
```python
Error: GEMINI_API_KEY not found
Solution: Create .env file with EMINI_API_KEY=your_key_here
```

**File Not Found:**
```python
Error: Could not find input file at: data/code.py
Solution: Ensure code.py exists in the data/ directory
```
**Connection Error:**
```python
Error: Failed to connect to the API. Check your internet connection.
Solution: Verify internet connectivity and API service status
```
**Timeout Error:**
```python
Error: Request timed out. Please try again.
Solution: Retry the request or check API service status
```

**Invalid Response Format:**
```python
Error: Invalid response format from the API.
Solution: Check API quota limits and service status
```
## Configuration Tips

**Prompt Design Guidelines:**
- **Be specific:** Use numbered requirements for structured output
- **Set context:** Use role-based system instructions
- **Request multiple dimensions**: Ask for strengths, weaknesses, and optimization
- **Include formatting guidelines:** Specify desired output structure

**Model Configuration:**
- **gemini-3-flash-preview:** Fast, cost-effective for resume analysis
- **Temperature 1.0:** Balanced creativity for improvements and rewording
- **Temperature 0.3-0.5:** More consistent, factual analysis only
- **Temperature 1.0-1.5:** More creative suggestions and alternative phrasings

**File Preparation:**
- **Use clean PDFs:** Avoid scanned images or complex formatting
- **Plain text works best:** Consider converting to .txt for best results
- **Remove sensitive info:** Mask personal details for testing
- **One-column layout:** Avoid multi-column resumes for better parsing

**Resume Optimization Tips:**
- **Use metrics:** Quantify achievements with numbers and percentages
- **Action verbs:** Start bullet points with strong action verbs
- **Keywords:** Include industry-specific technical terms
- **ATS-friendly:** Use standard headers and simple formatting
- **Tailored content:** Customize for each job application

**💡 Tips for Best Results**
- **Well-formatted input:** Clean, properly structured resumes yield better analysis
- **Include context:** Docstrings and detailed descriptions improve feedback
- **Focus on metrics:** Quantifiable achievements get stronger recognition
- **Iterative refinement:** Apply suggestions and re-analyze for continuous improvement
- **Job-specific:** Tailor resume to specific job descriptions for best matching

## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your AI story platform

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community
- All contributors and users

---

Happy Job Hunting! 📄✨

Remember: Effective resume analysis starts with clear prompts and expert role instructions. Experiment with different analysis dimensions and temperature settings to discover what works best for your specific career development needs!

