import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

# Load environment variables from .env file (if present)
load_dotenv()

# Constants
# Model selection and generation temperature for more deterministic output
TARGET_MODEL = "gemini-3-flash-preview"
TEMPERATURE = 1

# Relative path to the resume file to analyze
TARGET_FILE = "data/resume.pdf"


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
    """Create a detailed prompt for resume analysis.

    Instructs the GenAI model to analyze the resume and provide
    specific feedback on strengths, improvements, and ATS compatibility.

    Args:
        content: The resume text content to analyze.

    Returns:
        str: A formatted prompt for the GenAI model.
    """
    user_prompt = f"""

        Improve the following resume professionaly.
        Also provide:
        1. Key strengths and skills highlighted in the resume.
        2. Areas for improvement in terms of content, structure, and formatting.
        3. ATS (Applicant Tracking System) compatibility analysis and suggestions.

        Resume content:
        {content}
        """
    return user_prompt

def read_resume_from_file(file_path: str) -> str:
    """Read and return the contents of a resume file.

    Supports both absolute and workspace-relative paths. When a relative
    path is provided, it is resolved relative to this script's directory.
    
    For PDF files, uses pypdf to extract text. For other files, reads as plain text.

    Args:
        file_path: Relative or absolute path to the resume file.

    Returns:
        str: The file contents of the resume as a string.

    Raises:
        FileNotFoundError: When the resolved path does not exist.
        ValueError: When there's an error reading or extracting from the file.
    """
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find input file at: {file_path}")
    
    try:
        # Handle PDF files
        if file_path.lower().endswith('.pdf'):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        # Handle text files
        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")
    except Exception as e:
        raise ValueError(f"Error reading file at {file_path}: {str(e)}")


def analyze_resume(client: 'genai.Client', prompt: str) -> str:
    """Call the GenAI model to analyze a resume and return the feedback.

    The function provides a system instruction to the model to position it as
    an expert resume writing assistant. Common API errors are handled and
    returned as readable messages to keep the CLI interactive.

    Args:
        client: Authenticated GenAI client instance.
        prompt: The user-facing prompt produced by `create_user_prompt`.

    Returns:
        str: The model's response text with resume feedback, or an error string describing the failure.
    """
    system_instructions = "You are an expert resume writing assistant. Please analyze the following resume:"
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
    """Script entry point: read resume file, build prompt, call model, and print analysis.

    This function orchestrates the resume analysis workflow:
    1. Loads environment variables
    2. Reads the resume file (supports PDF and text formats)
    3. Creates a detailed analysis prompt
    4. Calls the GenAI model for expert feedback
    5. Displays the analysis results
    """
    print("--- Welcome to your AI Resume Analyzer! ---")
    print("Analyzing resume from file:", TARGET_FILE)

    # Read resume to analyze
    resume_content = read_resume_from_file(TARGET_FILE)

    # Build the prompt that instructs the model how to analyze the resume
    user_prompt = create_user_prompt(resume_content)

    # Initialize client and make the API call
    client = create_genai_client()
    print("Analyzing resume... Please wait.\n")
    result = analyze_resume(client, user_prompt)

    # Print a readable separator and the model's output
    print("-" * 60)
    print(result)
    print("-" * 60)


if __name__ == "__main__":
    main()