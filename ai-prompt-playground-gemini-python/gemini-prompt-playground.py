"""Gemini Prompt Playground

An interactive tool for experimenting with different prompt configurations,
system instructions, and temperature settings using Google's Gemini API.

Features:
    - Compare multiple prompts with different configurations side-by-side
    - A/B test various temperature and top_p values to understand their impact
    - Chain prompts for multi-step workflows and iterative refinement
    - Evaluate outputs with basic metrics (word count, unique words)

Usage:
    Run the script and choose between two modes:
    1. Test and Compare Prompts: Compare two outputs with different configurations
    2. Prompt Chaining Demo: Generate output and iteratively refine it

Requirements:
    - GEMINI_API_KEY environment variable set in .env file
    - google-genai package installed
    - python-dotenv package installed

Author: AI Code Examples
Date: 2026
"""

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
# This file should contain GEMINI_API_KEY=your_api_key_here
load_dotenv()

def create_genai_client():
    """Create and return an authenticated Gemini AI client instance.
    
    Retrieves the API key from environment variables and initializes
    the Gemini client for making API calls.
    
    Returns:
        genai.Client: An authenticated client instance for interacting with Gemini API.
        
    Raises:
        ValueError: If GEMINI_API_KEY is not found in environment variables.
    """
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_output(client, user_prompt, system_prompt, temperature, top_p):
    """Generate AI content using Gemini API with specified configuration.
    
    Args:
        client (genai.Client): The Gemini API client instance.
        user_prompt (str): The user's input prompt for content generation.
        system_prompt (str): System instruction to guide the model's behavior.
        temperature (float): Controls randomness (0.0-1.0). Higher values produce more creative outputs.
        top_p (float): Nucleus sampling parameter (0.0-1.0). Controls diversity of token selection.
    
    Returns:
        str: The generated text from the model, or an error message if generation fails.
    """
    # Configure generation parameters
    config = genai.types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=temperature,
        top_p=top_p
    )
    try:
        # Generate content using Gemini Flash model
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=config,
            contents=user_prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def evaluate_outputs(outputs):
    """Display basic metrics for comparing multiple AI-generated outputs.
    
    Provides word count and unique word count for each output to help
    assess verbosity and vocabulary diversity.
    
    Args:
        outputs (list[str]): List of AI-generated text outputs to evaluate.
    """
    print("\n--- Evaluation Metrics ---")
    # Calculate and display basic metrics for each output
    for i, out in enumerate(outputs):
        print(f"Output {i+1}: {len(out.split())} words, {len(set(out.split()))} unique words")
    print("You can also manually compare the outputs above for relevance, tone, and creativity.")

def prompt_chaining(client, initial_prompt, system_prompt, temperature, top_p):
    """Demonstrate prompt chaining by generating output and refining it with follow-up instructions.
    
    This function illustrates a two-step workflow where the output from the first
    generation is fed back into the model along with refinement instructions.
    
    Args:
        client (genai.Client): The Gemini API client instance.
        initial_prompt (str): The initial user prompt for the first generation.
        system_prompt (str): System instruction to guide the model's behavior.
        temperature (float): Controls randomness in generation.
        top_p (float): Nucleus sampling parameter.
    """
    # Step 1: Generate initial output
    first_output = generate_output(client, initial_prompt, system_prompt, temperature, top_p)
    print("\n--- First Output (Step 1) ---")
    print(first_output)
    
    # Step 2: Get follow-up instruction and chain with previous output
    followup = input("\nEnter a follow-up instruction to chain (e.g., 'Make it more concise'): ")
    chained_output = generate_output(client, followup + "\n\n" + first_output, system_prompt, temperature, top_p)
    print("\n--- Chained Output (Step 2) ---")
    print(chained_output)

def main():
    """Main entry point for the Gemini Prompt Playground application.
    
    Provides an interactive menu for users to choose between:
    1. Comparing prompts with different configurations
    2. Testing prompt chaining workflows
    """
    print("=== Gemini Prompt Playground ===")
    print("1. Test and Compare Prompts")
    print("2. Prompt Chaining Demo")
    choice = input("Choose an option (1/2): ").strip()
    
    # Initialize Gemini client
    client = create_genai_client()

    if choice == "1":
        # Mode 1: Compare two different prompt configurations
        # Collect user inputs for comparison test
        user_prompt = input("Enter your USER prompt: ")
        system_prompt1 = input("Enter SYSTEM prompt 1 (or leave blank for default): ") or "You are a helpful assistant."
        system_prompt2 = input("Enter SYSTEM prompt 2 (or leave blank for default): ") or "You are a creative assistant."
        temp1 = float(input("Temperature for output 1 (e.g., 0.7): ") or "0.7")
        temp2 = float(input("Temperature for output 2 (e.g., 0.3): ") or "0.3")
        top_p1 = float(input("top_p for output 1 (e.g., 0.9): ") or "0.9")
        top_p2 = float(input("top_p for output 2 (e.g., 0.7): ") or "0.7")

        # Generate and display first output with config 1
        print("\n--- Generating Output 1 ---")
        out1 = generate_output(client, user_prompt, system_prompt1, temp1, top_p1)
        print(out1)
        
        # Generate and display second output with config 2
        print("\n--- Generating Output 2 ---")
        out2 = generate_output(client, user_prompt, system_prompt2, temp2, top_p2)
        print(out2)
        
        # Evaluate and compare both outputs
        evaluate_outputs([out1, out2])

    elif choice == "2":
        # Mode 2: Demonstrate prompt chaining workflow
        initial_prompt = input("Enter your initial USER prompt: ")
        system_prompt = input("Enter SYSTEM prompt (or leave blank for default): ") or "You are a helpful assistant."
        temperature = float(input("Temperature (e.g., 0.7): ") or "0.7")
        top_p = float(input("top_p (e.g., 0.9): ") or "0.9")
        prompt_chaining(client, initial_prompt, system_prompt, temperature, top_p)
    else:
        # Handle invalid menu choice
        print("Invalid choice.")

# Entry point: Run main() only when script is executed directly (not imported)
if __name__ == "__main__":
    main()
