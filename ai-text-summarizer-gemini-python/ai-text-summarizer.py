"""
AI Text Summarizer using Google Gemini API

This module provides functionality to generate multiple types of text summaries
using the Google Gemini API. It supports three summarization styles:
- Bullet point summary (5 key points)
- Executive summary (concise professional summary)
- One-line summary (single impactful sentence)

Requirements:
    - GEMINI_API_KEY environment variable must be set
    - Internet connection for API calls
    - Input text file in the project directory

Example:
    python gemini-text-summarizer.py
"""

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL: str = "gemini-3-flash-preview"  # Gemini model for text generation
TARGET_FILE: str = "sample_article.txt"  # Input file containing text to summarize

BULLET_PROMPT: str = """
Summarize the following article into 5 bullet points:
"""

EXECUTIVE_PROMPT: str = """
Write a concise executive summary of the following article:
"""

ONE_LINE_PROMPT: str = """
Summarize the article in one single impactful sentence:
"""


def create_genai_client() -> genai.Client:
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    return genai.Client()

def create_summary(client: genai.Client, text: str, prompt_template: str) -> str:
    """
    Generates a summary of the given text using the Gemini API.
    
    This function combines a prompt template with the input text and sends it to
    the Gemini API for processing. The type of summary depends on the prompt_template
    provided (bullet points, executive summary, or one-line summary).
    
    Args:
        client (genai.Client): Authenticated Gemini API client.
        text (str): The text content to be summarized.
        prompt_template (str): The prompt instruction that defines the summary style.
    
    Returns:
        str: The generated summary text from the API, or an error message if the
             request fails.
    
    Raises:
        ValueError: Invalid input or API configuration error.
        AttributeError: API response format error.
        ConnectionError: Connection issues with the Gemini API.
        TimeoutError: API request exceeds timeout.
        Exception: Any other unexpected errors during API communication.
    """
    user_prompt: str = create_user_prompt(text, prompt_template)
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            contents=f"{user_prompt}"
        )
        return response.text
    except ValueError as ve:
        error_msg: str = f"Invalid input or API configuration error: {ve}"
        print(f"Error: {error_msg}")
        return error_msg
    except AttributeError as ae:
        error_msg: str = f"API response format error: {ae}"
        print(f"Error: {error_msg}")
        return error_msg
    except ConnectionError as ce:
        error_msg: str = f"Connection error while calling Gemini API: {ce}"
        print(f"Error: {error_msg}")
        return error_msg
    except TimeoutError as te:
        error_msg: str = f"API request timed out: {te}"
        print(f"Error: {error_msg}")
        return error_msg
    except Exception as e:
        error_msg: str = f"An unexpected error occurred while calling Gemini API: {e}"
        print(f"Error: {error_msg}")
        return error_msg

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

def create_user_prompt(text: str, prompt_template: str) -> str:
    """
    Combines a prompt template with input text to create a complete user prompt.
    
    Concatenates the prompt template and text with a newline separator to form
    the complete instruction for the Gemini API.
    
    Args:
        text (str): The input text content to be summarized.
        prompt_template (str): The instruction template for generating summaries.
    
    Returns:
        str: The complete prompt combining template and text.
    """
    user_prompt: str = f"{prompt_template}\n{text}" 
    return user_prompt

def main() -> None:
    """
    Main entry point for the AI Text Summarizer application.
    
    This function orchestrates the summarization workflow:
    1. Reads input text from a file
    2. Initializes the Gemini API client
    3. Generates three different types of summaries:
       - Bullet point summary (5 key points)
       - Executive summary (professional concise summary)
       - One-line summary (single impactful sentence)
    4. Displays results to the user
    """
    print("--- Welcome to your AI Text Summarizer! ---")
    print("Reading input text from file...")
    user_text: str = read_text_from_file(TARGET_FILE)
    
    print("Generating Basic summary...Please wait...")
    
    # Initialize the Gemini API client
    client: genai.Client = create_genai_client()
    
    # Generate and display bullet point summary
    bullet_summary: str = create_summary(client, user_text, BULLET_PROMPT)
    print("\n--- Bullet Point Summary ---")
    print(bullet_summary)

    # Generate and display executive summary
    executive_summary: str = create_summary(client, user_text, EXECUTIVE_PROMPT)
    print("\n--- Executive Summary ---")
    print(executive_summary)

    # Generate and display one-line summary
    print("\n--- One Line Summary ---")
    one_line_summary: str = create_summary(client, user_text, ONE_LINE_PROMPT)
    print(one_line_summary)

if __name__ == "__main__":
    main()
