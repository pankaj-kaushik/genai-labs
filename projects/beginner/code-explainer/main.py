
"""
Code Explainer - CLI helper to analyze Python code using Gemini

This module reads a Python source file, constructs a structured prompt,
and asks the Gemini model to explain the code: overview, key components,
potential issues, and complexity analysis. The script is designed for
interactive command-line use and is tolerant of API errors (returns
readable error messages instead of raising).

Usage:
    python main.py

Requirements:
    - google-genai
    - python-dotenv
    - GEMINI_API_KEY environment variable (or set in .env)
"""

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file (if present)
load_dotenv()

# Constants
# Model selection and generation temperature for more deterministic output
TARGET_MODEL = "gemini-3-flash-preview"
TEMPERATURE = 0.2
# Relative path to the example code file to analyze
TARGET_FILE = "data/code.py"


def create_genai_client() -> 'genai.Client':
    """Initialize and return an authenticated GenAI client.

    The client relies on the `GEMINI_API_KEY` being available in the
    environment (for example via a local `.env` file loaded above).

    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    print("Creating Gen AI client...")
    return genai.Client()

def create_user_prompt(content: str) -> str:
    """Build a structured prompt instructing the model how to analyze code.

    Args:
        content: The Python source code to be analyzed (as a single string).

    Returns:
        A prompt string that includes the code block and a numbered list of
        required analysis sections (overview, component explanations,
        improvements, and complexity analysis).
    """
    # Using a fenced code block and explicit numbered requirements helps
    # the model produce structured, easy-to-read output.
    user_prompt = f"""
        Analyze this Python code and provide the requested sections.

        ```python
        {content}
        ```

        Please provide:
        1. A short overview of what the code does.
        2. Explanation of key components and program flow.
        3. Any potential issues, bugs, or suggested improvements.
        4. Time and space complexity analysis for the main functions.
        """
    return user_prompt

def read_code_from_file(file_path: str) -> str:
    """Read and return the contents of a file.

    Supports both absolute and workspace-relative paths. When a relative
    path is provided, it is resolved relative to this script's directory.

    Args:
        file_path: Relative or absolute path to the target file.

    Returns:
        The file contents as a string.

    Raises:
        FileNotFoundError: When the resolved path does not exist.
    """
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")


def explain_code(client: 'genai.Client', prompt: str) -> str:
    """Call the GenAI model to analyze code and return the textual result.

    The function provides a short `system_instruction` to the model to
    encourage an expert-level analysis. Common API errors are handled and
    returned as readable messages to keep the CLI interactive.

    Args:
        client: Authenticated GenAI client instance.
        prompt: The user-facing prompt produced by `create_user_prompt`.

    Returns:
        The model's response text, or an error string describing the failure.
    """
    system_instructions = "You are an expert Senior Developer. Please analyze the following Python code:"
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instructions,
                temperature=TEMPERATURE
            ),
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
        return f"An unexpected error occurred while calling the GenAI API: {e}"

def main() -> None:
    """Script entry point: read file, build prompt, call model, and print result."""
    print("--- Welcome to your AI Code Explainer! ---")
    print("Analyzing code from file:", TARGET_FILE)

    # Read source code to analyze
    code_content = read_code_from_file(TARGET_FILE)

    # Build the prompt that instructs the model how to analyze the code
    user_prompt = create_user_prompt(code_content)

    # Initialize client and make the API call
    client = create_genai_client()
    print("Explaining code... Please wait.\n")
    result = explain_code(client, user_prompt)

    # Print a readable separator and the model's output
    print("-" * 60)
    print(result)
    print("-" * 60)


if __name__ == "__main__":
    main()