"""
Study Buddy - AI Learning Assistant

Interactive CLI that uses Google Gemini (via `google-genai`) to explain
concepts at different expertise levels, provide analogies, key takeaways,
and short quiz questions. Configuration is read from a local `.env` file
via `python-dotenv`; ensure `GEMINI_API_KEY` is set before running.

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

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL = "gemini-3-flash-preview"

def create_genai_client() -> 'genai.Client':
    """Initialize and return an authenticated GenAI client.

    The client uses the `GEMINI_API_KEY` from the environment (or `.env`).

    Returns:
        genai.Client: Authenticated GenAI client instance.
    """
    print("\nCreating Gen AI client...")
    return genai.Client()

def create_prompt(topic: str, level: str) -> str:
    """Build a system-style prompt instructing the model how to teach a topic.

    Args:
        topic: Concept or subject to explain.
        level: One of "Beginner", "Intermediate", or "Advanced" which
            controls the tone and depth of the explanation.

    Returns:
        A formatted prompt string suitable for sending to the model.
    """
    level_instructions = {
        "Beginner": "Use simple analogies, avoid jargon, and explain like I'm 10.",
        "Intermediate": "Use standard technical terms with brief definitions and practical examples.",
        "Advanced": "Provide a deep dive into architecture, nuances, and edge cases. Assume I'm a pro."
    }

    # Choose instructions based on requested level; default to concise guidance
    constraints = level_instructions.get(level, "Present the topic clearly and concisely.")

    user_prompt = f"""
You are an expert Study Buddy.
Task: Explain the concept of '{topic}' at a {level} level.
Constraints: {constraints}
Format: Use Markdown for clarity (bolding, bullet points, short examples, and a 2-3 question quiz).
"""
    return user_prompt


def explain_concept(client: 'genai.Client', prompt: str) -> str:
    """Request an explanation from the model and return the text result.

    The response is expected to include an explanation, analogies, key
    takeaways, and a short quiz. API errors are caught and returned as a
    readable string so the CLI remains user-friendly.

    Args:
        client: Authenticated GenAI client.
        prompt: Prompt produced by `create_prompt` describing task and format.

    Returns:
        The model's textual response, or an error message on failure.
    """
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,  # using the fast flash model for responsiveness
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred while calling the GenAI API: {e}"

def get_user_input() -> tuple[str, str]:
    """Prompt the user for a topic and desired learning level.

    Returns a tuple: (topic, level).
    """
    topic = input("What concept would you like to learn today? ")
    level = input("What is your learning level? (Beginner/Intermediate/Advanced) ")
    return topic, level

def main() -> None:
    print("--- Welcome to your AI Study Buddy! ---")
    print("Please enter the details of the topic you want to learn about.")
    print("-" * 60)

    topic, level = get_user_input()

    print("\nCreating prompt...")
    user_prompt = create_prompt(topic, level)

    client = create_genai_client()
    print(f"\nAnalyzing '{topic}'... Please wait.\n")
    explanation = explain_concept(client, user_prompt)

    print("-" * 60)
    print(explanation)
    print("-" * 60)


if __name__ == "__main__":
    main()