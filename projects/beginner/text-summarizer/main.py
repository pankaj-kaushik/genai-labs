"""
Text Summarizer - An AI-Powered Text Summarization Tool

This module provides functionality to automatically summarize text documents
using Google's Gemini API. It reads text from files, processes them through
the Gemini model, and generates concise summaries in bullet-point format.

Usage:
    python main.py
    
Requirements:
    - google-genai library
    - python-dotenv library
    - GEMINI_API_KEY environment variable
    - input.txt file in the same directory
"""

# Summarizer.py
# A simple script to demonstrate the use of Google Gen AI API for text summarization.
# It initializes the environment, creates a client, and generates a summary for a given text.
# Make sure to set the GEMINI_API_KEY in your environment variables.
# User Text (from file) -> Python Code -> Gemini API -> Summary Output(written to file)

from dotenv import load_dotenv
from google import genai
import os

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL = "gemini-3-flash-preview"
TARGET_FILE = "input.txt"

def create_genai_client():
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    print("Creating Gen AI client...")
    return genai.Client()

def basic_summary(client, content):
    """
    Generate a brief summary for the provided text using the Gemini model.

    This function sends the provided text to the Gemini model (using the
    model defined by `TARGET_MODEL`) and returns the generated summary text.
    Errors during generation are caught and returned as human-readable strings
    instead of being raised.

    Args:
        client (genai.Client): An authenticated GenAI client instance.
        content (str): The text content to be summarized.

    Returns:
        str: The AI-generated summary, or an error message if the call fails.
    """
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL, contents=f"Summarize this in one line: {content}"
        )
        return response.text
    except ValueError as ve:
        error_msg = f"Invalid input or API configuration error: {ve}"
        print(f"Error: {error_msg}")
        return error_msg
    except AttributeError as ae:
        error_msg = f"API response format error: {ae}"
        print(f"Error: {error_msg}")
        return error_msg
    except ConnectionError as ce:
        error_msg = f"Connection error while calling Gemini API: {ce}"
        print(f"Error: {error_msg}")
        return error_msg
    except TimeoutError as te:
        error_msg = f"API request timed out: {te}"
        print(f"Error: {error_msg}")
        return error_msg
    except Exception as e:
        error_msg = f"An unexpected error occurred while calling Gemini API: {e}"
        print(f"Error: {error_msg}")
        return error_msg

def professional_summary(client, user_prompt):
    """
    Generates a professional summary using the Gemini API with system instructions.
    
    This function sends the provided prompt along with specific system instructions
    to guide the Gemini model in producing a high-quality, professional summary.
    It includes error handling for API failures and network issues.
    
    Args:
        client (genai.Client): An authenticated GenAI client instance.
        prompt (str): Instructional prompt text to guide the model's output.
        content (str): The text content to be summarized.

    Returns:
        str: The AI-generated professional summary, or an error message if
             the call fails.
    """
    
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            contents=f"{user_prompt}"
        )
        return response.text
    except ValueError as ve:
        error_msg = f"Invalid input or API configuration error: {ve}"
        print(f"Error: {error_msg}")
        return error_msg
    except AttributeError as ae:
        error_msg = f"API response format error: {ae}"
        print(f"Error: {error_msg}")
        return error_msg
    except ConnectionError as ce:
        error_msg = f"Connection error while calling Gemini API: {ce}"
        print(f"Error: {error_msg}")
        return error_msg
    except TimeoutError as te:
        error_msg = f"API request timed out: {te}"
        print(f"Error: {error_msg}")
        return error_msg
    except Exception as e:
        error_msg = f"An unexpected error occurred while calling Gemini API: {e}"
        print(f"Error: {error_msg}")
        return error_msg

def read_text_from_file(file_path):
    """
    Reads text content from a file with relative or absolute path support.
    
    If a relative path is provided, it is treated as relative to this script's
    directory. This function includes error handling for missing files.
    
    Args:
        file_path (str): The path to the file (relative or absolute).
        
    Returns:
        str: The complete text content of the file.
        
    Raises:
        FileNotFoundError: If the specified file cannot be found. The
            raised message includes the resolved absolute path.
    """
    # If a relative path is provided, treat it as relative to this script's directory.
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")

def get_prompt():
    """
    Construct a reusable instructional prompt for the Gemini model.

    The returned prompt contains clear guidance to produce a short,
    professional, beginner-friendly summary in 4-5 bullet points. This
    function does not accept any arguments; the calling code appends the
    actual text to summarize when sending the request.

    Returns:
        str: A prompt string describing the desired summarization style.
    """
    user_prompt = f"You are a professional editor. Summarize the following text in simple language.\nUse 4-5 bullet points.\nMake it easy for beginners to understand.\n"
    return user_prompt


def main():
    """
    Main entry point for the Text Summarizer application.
    Orchestrates the text summarization workflow by:
    1. Reading input text from a target file
    2. Retrieving the summarization prompt
    3. Initializing the generative AI client
    4. Generating a basic summary of the input text
    5. Generating a professional summary using the prompt
    Prints progress messages and outputs summaries to the console.
    Returns:
        None
    """
    
    print("--- Welcome to your Text Summarizer Writer! ---")
    print("Reading input text from file...")    
    user_text = read_text_from_file(TARGET_FILE)
    
    print("Prompt Used...")
    input_prompt = get_prompt()
    print(input_prompt)

    client = create_genai_client()
    print("Generating Basic summary...")
    basic_summary_output = basic_summary(client, user_text)
    print("Basic Summary:\n", basic_summary_output)

    print("Generating Professional summary...")
    professional_summary_output = professional_summary(client, input_prompt)
    print("Professional Summary:\n", professional_summary_output)

if __name__ == "__main__":
    main()  
    