# 📄 AI Text Summarizer Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Text Summarizer** - your intelligent assistant for condensing large documents into digestible insights!
This **beginner-friendly** project demonstrates how to leverage **Large Language Models (LLMs)** with **prompt engineering** techniques to generate multiple summary formats from a single text source.

Instead of manually reading lengthy articles, this system allows you to:

- 📍 **Extract key points** in bullet format for quick scanning
- 📄 **Generate executive summaries** for professional contexts
- ✨ **Create one-line summaries** for rapid comprehension
- 🎯 **Compare outputs** to understand how prompt design influences results
- 🔄 **Process any text** quickly and efficiently

Perfect for beginners learning AI integration, Prompt Engineering, and building practical NLP applications!

## 🚀 What This Project Does
- Reads text content from files automatically
- Generates three distinct summary formats from the same content
- Demonstrates how **prompt variations → output variations**
- Handles errors gracefully with comprehensive exception handling
- Provides a clean CLI interface for easy interaction
- Uses Google's Gemini LLM for high-quality summarization

The tool generates three powerful summary types:

### 📍 Bullet Point Summary
- Extracts **5 key points** from the article
- Perfect for **quick reference** and presentations
- Maintains essential information in scannable format
- Great for **meeting notes** and study guides

### 📄 Executive Summary
- Provides a **concise professional overview**
- Ideal for **business reports** and proposals
- Captures main themes and conclusions
- Perfect for **stakeholders** and decision-makers

### ✨ One-Line Summary
- Distills entire content into **one impactful sentence**
- Great for **headlines** and quick sharing
- Tests the model's ability to identify core message
- Perfect for **social media** and abstracts

## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🔌 How to integrate **Gemini LLM APIs** using Python
- 📝 How **prompt design** affects LLM outputs
- 🎯 How to implement **Zero-Shot prompting** techniques
- 🔄 How to handle **file I/O** operations in Python
- ⚠️ How to implement **error handling** for API calls
- 🏗️ How to structure **modular, reusable code**
- 🔐 How to manage **API keys** securely with environment variables
- 🧪 **Comparative prompt experimentation** methodologies

This project strengthens both **AI integration** skills and **practical software development** best practices.

## 🏢 Industry Use Cases
- 📚 **Research & Academia**
  - Academic paper summarization
  - Literature review automation
  - Research digest generation

- ⚖️ **Legal & Compliance**
  - Contract review summaries
  - Case law analysis
  - Regulatory document processing

- 📰 **Media & Publishing**
  - News aggregation systems
  - Content curation platforms
  - Editorial workflow automation

- 💼 **Enterprise & Business**
  - Meeting transcript summarization
  - Knowledge-base documentation
  - Report generation
  - Email digest creation

- 🏥 **Healthcare**
  - Medical record summarization
  - Clinical trial documentation
  - Patient history digests

- 🎓 **Education & Training**
  - Study material condensation
  - Course content summaries
  - Learning resource curation

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> File Reader -> Text Extraction -> Prompt Builder (3 types) -> Gemini LLM API -> Response Processor -> Formatted Output Display
```
Detailed Flow:\
1. Application starts - User launches the CLI application
2. File reading - System reads text from ```sample_article.txt```
3. Prompt construction - Three different prompts are prepared:
- Bullet point prompt
- Executive summary prompt
- One-line summary prompt
4. API client initialization - Gemini client is created with API key
5. Sequential generation - Each prompt is sent to Gemini API
6. Response processing - API responses are formatted
7. Error handling - Catches and handles various exceptions
8. Output display - Results are printed to console in organized sections

## ▶️ How to Run the Project
### Step 1: Update ```sample_article.txt``` File
Copy and paste content of your article in ```sample_article.txt``` file

### Step 2: Run Application
```bash
python ai-text-summarizer.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
The application uses zero-shot prompting, where instructions are provided without examples:
```python
BULLET_PROMPT = """Summarize the following article into 5 bullet points:"""
```
**Why Zero-Shot?**

- Relies on model's pre-trained knowledge
- No need for example summaries
- Flexible across different content types
- Simpler prompt construction

### Task-Specific Prompt Design
Each prompt is optimized for its specific output format:
```python
EXECUTIVE_PROMPT = """Write a concise executive summary of the following article:"""
```
**Key characteristics:**
- Clear, unambiguous instructions
- Specific format requirements
- Action-oriented verbs ("Summarize", "Write")
- No unnecessary complexity

### Constraint-Based Prompting
Prompts include explicit constraints for focused outputs:
```python
ONE_LINE_PROMPT = """Summarize the article in one single impactful sentence:"""
```
**Benefits:**
- Controls output length
- Ensures consistency
- Prevents verbose responses
- Focuses model on core message

### Comparative Experimentation
The tool demonstrates how different prompt styles produce different results:

- Structural variation: Bullet vs paragraph format
- Length variation: One-line vs executive summary
- Purpose variation: Quick reference vs professional overview
This approach teaches:

- How prompts influence output style
- How to select appropriate formats for use cases
- How to design prompts for specific needs

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
- 🌐 Web Interface with Streamlit
  - Drag-and-drop file upload
  - Real-time summary generation
  - Side-by-side comparison view
  - Export to PDF/Word
- 📄 Multi-Format Support
  - PDF document parsing
  - DOCX file processing
  - URL/web page scraping
  - Markdown file support
- 🎛️ Customizable Parameters
  - Adjustable summary length
  - Custom number of bullet points
  - Temperature control for creativity
  - Multiple language support
- 📊 Analytics & Metrics
  - Compression ratio calculation
  - Readability scores
  - Key entity extraction
  - Sentiment analysis
- 💾 Output Management
  - Save summaries to files
  - Export history
  - Batch processing mode
  - Compare multiple articles
- 🔄 Advanced Features
  - Multi-document summarization
  - Hierarchical summarization
  - Query-focused summaries
  - Abstractive vs extractive comparison
- 🎯 Domain-Specific Templates
  - Medical document summaries
  - Legal brief generation
  - Technical documentation
  - Financial report summaries
🔐 Enterprise Features
  - User authentication
  - Usage tracking
  - API rate limiting
  - Cost monitoring

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
- **Set constraints:** Define length, style, or structure requirements
- **Use action verbs:** "Summarize", "Extract", "Generate"
- **Test variations:** Experiment with different phrasings

Model Selection:
- **gemini-3-flash-preview:** Fast, cost-effective for summarization
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

Happy Summarizing! 🧠✨

Remember: Effective summarization starts with effective prompts. Experiment with different prompt styles to discover what works best for your specific content types and use cases!