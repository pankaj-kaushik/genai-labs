# 📝 AI Meeting Notes Generator Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Meeting Notes Generator** – your smart assistant for transforming lengthy meeting transcripts into actionable, concise notes!  
This **beginner-friendly** project demonstrates how to leverage **Large Language Models (LLMs)** and **prompt engineering** to automatically generate structured meeting notes, action items, and executive summaries from raw meeting text.

Instead of manually sifting through transcripts, this tool enables you to:

- 📍 **Extract key discussion points** in bullet format
- ✅ **Generate action items** for follow-up
- 📄 **Create executive summaries** for quick review
- 🎯 **Compare outputs** to see how prompt design shapes results
- 🔄 **Process any meeting transcript** efficiently

Perfect for beginners learning AI integration, Prompt Engineering, and building practical NLP applications for productivity!

## 🚀 What This Project Does
- Reads meeting transcript from a file automatically
- Generates three distinct note formats from the same content
- Demonstrates how **prompt variations → output variations**
- Handles errors gracefully with robust exception handling
- Provides a clean CLI interface for easy use
- Uses Google's Gemini LLM for high-quality note generation

The tool generates three powerful output types:

### 📍 Key Discussion Points
- Extracts **5 main discussion points** from the meeting
- Ideal for **quick reference** and sharing
- Maintains essential information in scannable format

### ✅ Action Items
- Lists **clear, actionable tasks** assigned during the meeting
- Perfect for **follow-up** and accountability
- Helps teams stay organized

### 📄 Executive Summary
- Provides a **concise professional overview** of the meeting
- Captures main themes, decisions, and next steps
- Ideal for **stakeholders** and absent participants

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
- 🏢 **Corporate Meetings**
    - Board meeting notes
    - Project stand-up summaries
    - Client call recaps

- 🏫 **Education**
    - Lecture note generation
    - Study group summaries

- 🏥 **Healthcare**
    - Medical team meeting notes
    - Case discussion summaries

- ⚖️ **Legal**
    - Deposition and hearing summaries
    - Case meeting notes

- 📰 **Media & Journalism**
    - Interview recaps
    - Editorial meeting notes

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> File Reader -> Transcript Loader -> Prompt Builder (3 types) -> Gemini LLM API -> Response Processor -> Formatted Output Display
```
**Detailed Flow:**
1. Application starts - User launches the CLI application.
2. File reading - System reads text from `meeting_transcript.txt`.
3. Prompt construction - Three distinct prompts are prepared:
    - Key discussion points prompt
    - Action items prompt
    - Executive summary prompt
4. API client initialization - Gemini client is created using the API key from environment variables.
5. Sequential generation - Each prompt is sent to the Gemini API for note generation.
6. Response processing - API responses are parsed and formatted for display.
7. Error handling - Handles missing files, API key errors, connection issues, and timeouts gracefully.
8. Output display - Results are printed to the console in clearly labeled sections.

## ▶️ How to Run the Project
### Step 1: Update `meeting_transcript.txt` File
Copy and paste your meeting transcript into the `meeting_transcript.txt` file.

### Step 2: Run Application
```bash
python ai-meeting-notes-generator.py
```

## 🧠 Prompt Engineering Used
We have used the following prompt techniques to ensure the AI produces reliable, structured notes:

### 1. **Structured Output Prompting**
The prompt explicitly requests output in a specific JSON format with predefined schema:
```json
{
  "meeting_title": "", 
  "date": "", 
  "participants": [], 
  "key_points": [], 
  "action_items": [], 
  "decisions": []
}
```
This technique ensures:
- ✅ Consistent, parsable output structure
- ✅ Predictable data format for downstream processing
- ✅ Clear expectations for the LLM about required fields

### 2. **Zero-Shot Information Extraction**
The prompt uses a single, comprehensive instruction without providing examples:
```
"Extract key information from the following meeting transcript and provide the output in valid JSON format..."
```
**Why Zero-Shot?**
- No training examples needed
- Quick implementation for varied meeting types
- Leverages the LLM's pre-trained knowledge about meetings
- Flexible enough to handle different meeting formats

### 3. **Clear Task Definition**
The prompt begins with an explicit instruction verb: **"Extract"**
- Tells the model exactly what action to perform
- Reduces ambiguity in the task
- Improves consistency across multiple runs

### 4. **Format Specification**
The prompt explicitly states: **"provide the output in valid JSON format"**
- Ensures machine-readable output
- Prevents natural language responses
- Enables automatic parsing and error handling

### 5. **Multi-Field Information Extraction**
The prompt requests six distinct categories of information:
- **meeting_title**: Identifies the meeting's subject
- **date**: Extracts temporal information
- **participants**: Lists all attendees
- **key_points**: Summarizes main discussions
- **action_items**: Identifies follow-up tasks
- **decisions**: Captures agreed outcomes

This comprehensive extraction maximizes the value derived from each transcript.

### 6. **Template-Based Prompt Construction**
The code uses a modular approach with `create_user_prompt()` function:
```python
prompt = f"{prompt_template}\n{transcript_text}"
```
**Benefits:**
- Easy prompt modification without changing core logic
- Reusable template for different transcripts
- Separation of concerns (prompt design vs. application logic)
- Facilitates A/B testing of different prompt variations

### 7. **Response Post-Processing**
The implementation handles various response formats:
- Strips markdown code blocks (```json ... ```)
- Validates JSON structure
- Provides fallback error messages
- Ensures robust parsing regardless of LLM output variations

### Key Prompt Engineering Principles Applied:
✨ **Specificity**: Clear instructions with defined output format  
✨ **Structure**: Explicit schema reduces hallucination  
✨ **Clarity**: Simple, direct language without ambiguity  
✨ **Validation**: Built-in error handling for malformed responses  
✨ **Modularity**: Reusable templates for scalability

## 📌 Sample Output
```powershell
--- Welcome to your AI Meeting Notes Generator! ---
Initializing Google Gemini API client...
Reading meeting transcript from meeting_transcript.txt...
Generating structured meeting notes...

==================================================
MEETING NOTES
==================================================

{
    "meeting_title": "Project Proposal Review Meeting",
    "date": "Not specified",
    "participants": [
        "Moderator",
        "Alice",
        "Bob",
        "Charlie",
        "Dana"
    ],
    "key_points": [
        "Alice has completed the initial draft of the project proposal.",
        "Bob reviewed the proposal and provided feedback on the timeline.",
        "The team discussed the necessity of extending the testing phase duration.",
        "Dana has obtained the latest budget figures from the finance department.",
        "The project is currently on track with no identified blockers."
    ],
    "action_items": [
        "Alice to update the proposal to include additional time for the testing phase.",
        "Dana to circulate the latest budget figures to the team.",
        "The team to finalize the project proposal by Friday."
    ],
    "decisions": [
        "Agreed to allocate more time for the testing phase in the project timeline.",
        "Set the deadline for finalizing the proposal for this coming Friday."
    ]
}
```

## ✨ Future Enhancements
- 🌐 Web Interface with Streamlit
    - Drag-and-drop transcript upload
    - Real-time note generation
    - Side-by-side comparison view
    - Export to PDF/Word
- 📄 Multi-Format Support
    - PDF and DOCX transcript parsing
    - Audio-to-text integration
    - Markdown export
- 🎛️ Customizable Parameters
    - Adjustable number of key points
    - Custom action item formatting
    - Multi-language support
- 📊 Analytics & Metrics
    - Meeting duration and participation stats
    - Action item completion tracking
- 💾 Output Management
    - Save notes to files
    - Export history
    - Batch processing mode
- 🔄 Advanced Features
    - Multi-meeting summarization
    - Query-focused notes
    - Integration with calendar/task apps
- 🎯 Domain-Specific Templates
    - Agile stand-up notes
    - Board meeting summaries
    - Client call recaps
- 🔐 Enterprise Features
    - User authentication
    - Usage tracking
    - API rate limiting

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
Solution: Ensure meeting_transcript.txt exists in the project directory
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
- **Use action verbs:** "Extract", "List", "Summarize"
- **Test variations:** Experiment with different phrasings

Model Selection:
- **gemini-3-flash-preview:** Fast, cost-effective for note generation
- Consider other models for specialized needs

## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your AI productivity story

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community

---

Happy Note-Taking! 🧠✨

Remember: Effective meeting notes start with effective prompts. Experiment with different prompt styles to discover what works best for your meetings!