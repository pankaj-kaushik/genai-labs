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
- Generates **structured meeting notes in JSON format** with comprehensive information extraction
- Extracts **meeting title, date, participants, key points, action items, and decisions**
- Handles errors gracefully with robust exception handling
- Provides a clean CLI interface with progress feedback
- Uses Google's **Gemini 3 Flash Preview** model for fast, accurate note generation
- Implements **smart JSON parsing** to handle various response formats


## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🔌 How to integrate **Google Gemini API** using the official Python SDK
- 📝 How to design **structured output prompts** for consistent JSON responses
- 🎯 How to implement **Zero-Shot information extraction** techniques
- 🔄 How to handle **file I/O** operations with both relative and absolute paths
- ⚠️ How to implement **comprehensive error handling** with specific exception types
- 🏗️ How to structure **modular, well-documented code** with type hints
- 🔐 How to manage **API keys** securely using environment variables and dotenv
- 🧹 How to implement **response post-processing** to handle various LLM output formats
- ✅ How to add **input validation** for robust error prevention
- 📊 How to extract **multiple information categories** from unstructured text

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
User -> CLI Interface -> API Client Initialization -> File Reader -> Prompt Builder -> Gemini API -> JSON Parser -> Structured Output Display
```
**Detailed Flow:**
1. **Application Start** - User launches the CLI application with welcome message
2. **API Client Initialization** - Validates GEMINI_API_KEY and creates GenAI client
3. **File Reading** - Reads transcript from `meeting_transcript.txt` (supports relative/absolute paths)
4. **Input Validation** - Checks if transcript text is non-empty
5. **Prompt Construction** - Combines template with transcript using structured output format
6. **API Call** - Sends request to Gemini 3 Flash Preview model
7. **Response Validation** - Checks for empty responses
8. **JSON Extraction** - Strips markdown code blocks and parses JSON
9. **Error Handling** - Catches and handles:
    - Missing API key (ValueError)
    - File not found (FileNotFoundError)
    - Invalid JSON (JSONDecodeError)
    - API errors (Exception)
10. **Output Display** - Prints formatted JSON with success/error indicators

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
❌ Error: GEMINI_API_KEY environment variable is not set. Please set it in your .env file or environment.
Solution: Create .env file with GEMINI_API_KEY=your_api_key_here
```
**File Not Found:**
```python
❌ Error: Could not find input file at: /path/to/meeting_transcript.txt
Solution: Ensure meeting_transcript.txt exists in the same directory as the script
```
**Empty Transcript Error:**
```python
❌ Error: Meeting transcript text cannot be empty
Solution: Add content to meeting_transcript.txt file
```
**JSON Parsing Error:**
```python
⚠️  Warning: An error occurred during processing.
"error": "Failed to parse JSON response: ..."
Solution: Check the raw_response field in output for debugging, or try running again
```
**API Request Failed:**
```python
❌ Error: API request failed: ...
Solution: Check your internet connection, API key validity, and Gemini API status
```
**Client Initialization Error:**
```python
❌ Error: Failed to initialize GenAI client: ...
Solution: Verify your API key is valid and you have proper internet connectivity
```

## 📝 Configuration Tips

### Prompt Design Guidelines:
- **Be specific:** The current prompt explicitly defines the JSON structure
- **Use action verbs:** "Extract" is used to clearly indicate the task
- **Provide schema:** Include the exact JSON format expected
- **Test variations:** Modify `EXTRACT_INFO_PROMPT` in the code to experiment

### Model Selection:
- **gemini-3-flash-preview:** Currently configured - fast and cost-effective
- To change model: Update `TARGET_MODEL` constant in the code
- Alternative options: gemini-2.0-flash-exp, gemini-1.5-pro

### File Path Configuration:
- **Relative paths:** Script automatically resolves paths relative to its directory
- **Absolute paths:** Also supported for flexibility
- To change input file: Update `TARGET_FILE` constant

### Environment Variables:
- **Required:** `GEMINI_API_KEY` must be set in `.env` file or system environment
- **Optional:** Add other configuration variables as needed
- **Security:** Never commit `.env` file to version control

### Error Handling Customization:
- All functions raise specific exception types for precise error handling
- Main function catches and displays user-friendly error messages
- Modify exception handling in `main()` for custom behavior

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