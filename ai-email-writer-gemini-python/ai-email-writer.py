"""
Email Writer - AI Email and Message Generation Assistant

This module provides an interactive CLI to generate professional and
personalized emails and messages using Google's Gemini API. It reads
configuration from a local `.env` file (via `python-dotenv`) and expects
the GEMINI_API_KEY to be available in the environment when creating the
GenAI client.

Usage:
    python main.py

Requirements:
    - google-genai library
    - python-dotenv library
    - GEMINI_API_KEY environment variable (or set in a .env file)

Notes:
    - The code uses the `TARGET_MODEL` constant to select the Gemini model.
    - Errors from the GenAI client are caught and returned as strings by
      the helper functions so the CLI remains interactive-friendly.
"""

import os
from typing import Tuple, Optional
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL: str = "gemini-3-flash-preview"


def create_email_prompt(purpose: str, tone: str, recipient: str, key_points: str) -> str:
    """
    Constructs a structured prompt for generating personalized emails.
    
    This function creates a detailed prompt that instructs Gemini to generate
    professional and engaging emails based on user specifications.
    
    Args:
        purpose (str): The main purpose or intent of the email.
        tone (str): The desired tone (e.g., formal, casual, enthusiastic).
        recipient (str): Description of the recipient or recipient type.
        key_points (str): Key points to include in the email (comma-separated
            or a short text block). The function does not parse this string;
            it is included verbatim in the prompt.

    Returns:
        str: A formatted prompt string with clear instructions for the AI model
             including the requested response format (Subject/Body).
    """
    # We use a system-style prompt to guide Gemini's behavior
    email_prompt: str = f"""
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
    """
    return email_prompt

def get_user_input() -> Tuple[str, str, str, str]:
    """
    Collects email composition details from the user via interactive prompts.
    
    Returns:
        tuple: A tuple containing four strings in the order:
            (purpose, tone, recipient, key_points)
    """
    purpose: str = input("Enter purpose of the email or message: ")
    tone: str = input("Enter desired tone (e.g., formal, casual, enthusiastic): ")
    recipient: str = input("Enter recipient details (e.g., friend, colleague, client): ")
    key_points: str = input("Enter key points to include (separated by commas): ")
    return purpose, tone, recipient, key_points

def create_genai_client(model: str = TARGET_MODEL, config: Optional[genai.types.GenerateContentConfig] = None) -> genai.Client:
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    return genai.Client()

def generate_email(client: genai.Client, prompt: str) -> str:
    """
    Generates an email or message using the Gemini API.
    
    This function sends the composed prompt to the Gemini model with specific
    system instructions to ensure high-quality, professional email generation.
    It includes error handling for API failures.
    
    Args:
        client (genai.Client): An authenticated GenAI client instance.
        prompt (str): The formatted prompt containing purpose, tone,
            recipient, and key points.

    Returns:
        str: The AI-generated email or message content. If an error occurs
             while calling the API, the function catches the exception and
             returns a human-readable error string instead of raising.
    """
    system_instructions: str = "You are a helpful assistant that writes emails and messages."
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            config=genai.types.GenerateContentConfig(system_instruction=system_instructions),
            contents=prompt
        )
        return response.text
    except AttributeError:
        return "Error: Invalid response format from the API."
    except ValueError as e:
        return f"Invalid input value: {e}"
    except ConnectionError:
        return "Error: Failed to connect to the API. Check your internet connection."
    except TimeoutError:
        return "Error: Request timed out. Please try again."
    except Exception as e:
        return f"An error occurred: {e}"

def main() -> None:
    """
    Main entry point for the AI Email & Message Writer application.
    This function orchestrates the email/message generation workflow by:
    1. Displaying a welcome message to the user
    2. Collecting user input (purpose, tone, recipient, key_points)
    3. Creating an email prompt based on user specifications
    4. Initializing a GenAI client connection
    5. Generating the email/message content using AI
    6. Displaying the generated email/message to the user
    The function guides the user through an interactive process to create
    customized emails or messages with specific tone and purpose.
    Returns:
        None
    """
    
    print("--- Welcome to your AI Email & Message Writer! ---")
    print("Please provide details for the email/message you want to create.")
    purpose: str
    tone: str
    recipient: str
    key_points: str
    purpose, tone, recipient, key_points = get_user_input()
    print("Creating Email Prompt...")
    user_prompt: str = create_email_prompt(purpose, tone, recipient, key_points)
    client: genai.Client = create_genai_client()
    print("Generating email/message... Please wait.\n")
    result: str = generate_email(client, user_prompt)
    print("--- Generated Email/Message ---")
    print(result)
    print("-" * 30)

if __name__ == "__main__":
    main()