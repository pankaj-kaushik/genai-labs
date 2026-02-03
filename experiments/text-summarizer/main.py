# Summarizer.py
# A simple script to demonstrate the use of Google Gen AI API for text summarization.
# It initializes the environment, creates a client, and generates a summary for a given text.
# Make sure to set the GEMINI_API_KEY in your environment variables.
# User Text (from file) -> Python Code -> Gemini API -> Summary Output(written to file)

from dotenv import load_dotenv
from google import genai
import os

def create_genai_client():
    print("Creating Gen AI client...")
    return genai.Client()

def summarize_text(client, input_prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=input_prompt
    )   
    return response.text

def read_text_from_file(file_path):
    # If a relative path is provided, treat it as relative to this script's directory.
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")

def create_prompt(user_text):
    prompt = f"Summarize the following text in a concise manner:\n\n{user_text}\n\nSummary:"
    return prompt

if __name__ == "__main__":

    print("Running text summarization example...")

    # Initialize environment variables
    print("Loading environment variables...")
    load_dotenv()

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    print("API KEY:", os.getenv("GEMINI_API_KEY"))
    
    print("Reading input text from file...")    
    user_text = read_text_from_file('input.txt')
    
    print("Creating prompt...")
    input_prompt = create_prompt(user_text)

    client = create_genai_client()
    print("Generating summary...")
        
    summary = summarize_text(client, input_prompt)
    print("Summary:", summary)