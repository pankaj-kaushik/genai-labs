from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Constants for the target model and generation settings
TARGET_MODEL = "gemini-3-flash-preview"

def create_genai_client(model=TARGET_MODEL, config=None):
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    return genai.Client()

def generate_content(prompt, config=None):
    client = create_genai_client()
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            config=config,
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
    
def create_story_prompt(hero: str, genre: str, place: str, idea: str, age_group: str) -> str:
    
    story_prompt = f"""
    You are a professional children's story writer.

    Write a {genre} story for children aged {age_group}.

    Main Character: {hero}
    Place: {place}
    Main Idea/Lesson: {idea}

    Follow these steps internally:
    1. Create a magical and engaging setting.
    2. Introduce the character with personality traits.
    3. Present a small problem or conflict.
    4. Show how the character solves the problem.
    5. End with a happy resolution.
    6. Clearly state the moral starting with 'Moral:'.

    Constraints:
    - Use vocabulary suitable for {age_group}.
    - Keep tone positive and warm.
    - Story length: 400-500 words.
    - Avoid scary or violent elements.
    """
    return story_prompt

def get_user_input():
    character = input("Who is the main character of the story? (e.g., a brave rabbit, a curious child): ")
    genre = input("What genre do you want? (e.g., adventure, fantasy, mystery): ")
    place = input("Where does the story take place? (e.g., a magical forest, a bustling city): ")
    idea = input("What is the main idea or lesson of the story? (e.g., the importance of kindness, the value of curiosity): ")
    age = input("What is the target age group for the story? (e.g., 5-7, 8-10): ")
    return character, genre, place, idea, age

def generate_story(prompt):
    return generate_content(prompt)

def main():
    
    print("--- Welcome to your AI Magic Storybox!! ---")
    print("Please provide details for the story you want to create.")
    chracter, genre, place, idea, age = get_user_input()
    print("\nGenerating your story...please wait...")
    print("-" * 60)
    user_prompt = create_story_prompt(chracter, genre, place, idea, age)
    result = generate_story(user_prompt)
    print(result)
    print("-" * 60)

if __name__ == "__main__":
    main()