"""
AI Meeting Notes Generator using Google Gemini API

This module provides functionality to generate structured meeting notes using the Google Gemini API. It extracts key information from meeting transcripts and outputs it in a structured JSON format.

Requirements:
    - GEMINI_API_KEY environment variable must be set
    - Internet connection for API calls
    - Input text file in the project directory

Example:
    python ai_meeting_notes_generator.py
"""

from dotenv import load_dotenv
from google import genai
import json
import os

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL: str = "gemini-3-flash-preview"  # Gemini model for text generation
TARGET_FILE: str = "meeting_transcript.txt"  # Input file containing meeting transcript

# Prompts for information extraction
EXTRACT_INFO_PROMPT: str = """
Extract key information from the following meeting transcript and provide the output in valid JSON format:
{"meeting_title": "", "date": "", "participants": [], "key_points": [], "action_items": [], "decisions": []}

Meeting transcript:
"""

# Function to create a GenAI client

def create_genai_client() -> genai.Client:
    """
    Initializes and returns a Google GenAI client.
    
    This function creates a client instance for interacting with the Google Gemini API.
    The API key is automatically read from the GEMINI_API_KEY environment variable.
    
    Returns:
        genai.Client: An initialized Google GenAI client instance.
    
    Raises:
        ValueError: If GEMINI_API_KEY environment variable is not set.
        Exception: If client initialization fails for any other reason.
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set. "
            "Please set it in your .env file or environment."
        )
    
    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        raise Exception(f"Failed to initialize GenAI client: {str(e)}")

# Function to extract information and generate structured JSON

def extract_meeting_notes(client: genai.Client, text: str) -> dict:
    """
    Generates structured meeting notes from the given text using the Gemini API.
    
    This function uses multi-step prompting to extract key information from a meeting
    transcript and returns it in a structured JSON format including meeting title,
    participants, key points, action items, and decisions.
    
    Args:
        client (genai.Client): An initialized Google GenAI client instance.
        text (str): The meeting transcript text to analyze.
    
    Returns:
        dict: A dictionary containing structured meeting notes with the following keys:
            - meeting_title: Title or subject of the meeting
            - date: Date when the meeting occurred
            - participants: List of meeting participants
            - key_points: List of main discussion points
            - action_items: List of action items with assignees
            - decisions: List of decisions made during the meeting
            - error: Error message if processing fails
    
    Raises:
        ValueError: If the transcript text is empty or invalid.
    """
    if not text or not text.strip():
        raise ValueError("Meeting transcript text cannot be empty")
    
    user_prompt: str = create_user_prompt(text, EXTRACT_INFO_PROMPT)
    
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL, 
            contents=f"{user_prompt}"
        )
        
        if not response.text:
            return {"error": "Empty response received from Gemini API"}
        
        # Extract JSON from response (may contain markdown formatting)
        response_text = response.text.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:]  # Remove ```json
        if response_text.startswith('```'):
            response_text = response_text[3:]  # Remove ```
        if response_text.endswith('```'):
            response_text = response_text[:-3]  # Remove closing ```
        
        notes = json.loads(response_text.strip())
        return notes
        
    except json.JSONDecodeError as e:
        return {
            "error": f"Failed to parse JSON response: {str(e)}",
            "raw_response": response.text if 'response' in locals() else "No response"
        }
    except AttributeError as e:
        return {"error": f"Invalid API response structure: {str(e)}"}
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# Function to read text from a file

def read_text_from_file(file_path: str) -> str:
    """
    Reads text content from a file.
    
    Supports both absolute and relative file paths. Relative paths are resolved
    relative to the directory containing this script.
    
    Args:
        file_path (str): The path to the text file. Can be absolute or relative
                        to the script's directory.
    
    Returns:
        str: The complete text content of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist at the given path.
    """
    # If a relative path is provided, treat it as relative to this script's directory.
    if not os.path.isabs(file_path):
        base_dir: str = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")

# Function to create user prompt

def create_user_prompt(text: str, prompt_template: str) -> str:
    """
    Creates a complete user prompt by combining the prompt template with the input text.
    
    This helper function concatenates the prompt template with the actual meeting
    transcript text to create a complete prompt for the Gemini API.
    
    Args:
        text (str): The meeting transcript or input text to be analyzed.
        prompt_template (str): The prompt template containing instructions for the LLM.
    
    Returns:
        str: The complete prompt ready to be sent to the Gemini API.
    
    Raises:
        ValueError: If either text or prompt_template is empty.
    """
    if not prompt_template or not prompt_template.strip():
        raise ValueError("Prompt template cannot be empty")
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")
    
    return f"{prompt_template}\n{text}"

# Main function

def main() -> None:
    """
    Main entry point for the AI Meeting Notes Generator.
    
    This function orchestrates the entire workflow:
    1. Initializes the GenAI client
    2. Reads the meeting transcript from file
    3. Extracts and structures meeting notes using Gemini API
    4. Outputs the results in formatted JSON
    
    The function handles all errors gracefully and provides informative error messages
    to help diagnose issues.
    
    Raises:
        SystemExit: If a critical error occurs that prevents execution.
    """
    try:
        # Initialize the GenAI client
        print("--- Welcome to your AI Meeting Notes Generator! ---")
        print("Initializing Google Gemini API client...")
        client = create_genai_client()
        
        # Read the meeting transcript
        print(f"Reading meeting transcript from {TARGET_FILE}...")
        transcript = read_text_from_file(TARGET_FILE)
        
        # Extract meeting notes
        print("Generating structured meeting notes...")
        meeting_notes = extract_meeting_notes(client, transcript)
        
        # Output results
        print("\n" + "="*50)
        print("MEETING NOTES")
        print("="*50 + "\n")
        print(json.dumps(meeting_notes, indent=4, ensure_ascii=False))
        
        # Check if there was an error in processing
        if "error" in meeting_notes:
            print("\n⚠️  Warning: An error occurred during processing.")
            return
        
        print("\n✓ Meeting notes generated successfully!")
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please ensure the meeting transcript file exists.")
        raise SystemExit(1)
        
    except ValueError as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please check your configuration and input data.")
        raise SystemExit(1)
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        print("Please check your setup and try again.")
        raise SystemExit(1)

if __name__ == "__main__":
    main()