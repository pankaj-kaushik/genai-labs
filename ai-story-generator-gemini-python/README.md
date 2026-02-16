# 🧸✨ AI Story Generator Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Story Generator** for kids.
This **beginner-friendly** project demonstrates demonstrates how to use **structured prompting** and guided creativity techniques to generate safe, engaging, and age-appropriate children's stories using a **Large Language Model (LLM).**

Instead of random storytelling, this system uses carefully designed prompts to control:

- 🧍 Character
- 🎭 Genre
- 🎯 Moral
- 🎂 Age Group
- 📏 Story length
- 😊 Tone

Perfect for beginners learning Prompt Engineering and LLM APIs!

## 🚀 What This Project Does
- Take structured inputs(character, genre, place, lesson/idea, age group)
- Builds a guided, step-by-step story prompt
- Generates a coherent children's story
- Ensure age-appropriate vocabulary
- Ends with cleary defined moral lesson

The AI internally follows a structured storytelling flow:

- 🌍 Create setting
- 🧍 Introduce character
- ⚠️ Present conflict
- 🚀 Build adventure
- 🎉 Resolve conflict
- 📜 Deliver moral

All automatically generated using the **Gemini LLM.**

## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🧩 How to design **structured prompts** with constraints and step-by-step instructions
- 🧠 How to guide **LLM reasoning** using chain-of-thought prompting
- 🎛️ How to control **creativity** with explicit constraints (tone, length, vocabulary)
- 🔐 How to integrate **Google Gemini API** using the official Python SDK
- 📏 How to manage **output format** and tone for specific audiences
- 🛡️ How to design **safe AI** content for kids with age-appropriate controls
- ⚠️ How to implement **comprehensive error handling** for API calls (ConnectionError, TimeoutError, ValueError)
- 🔄 How to collect and validate **user inputs** through interactive CLI
- 🏗️ How to structure **modular functions** for maintainability
- 🔑 How to manage **API keys securely** using environment variables with dotenv

This project strengthens both **Prompt Engineering** fundamentals and **LLM API integration** skills.

## 🏢 Industry Use Cases
- 🎓 EdTech Platforms
  - Automated reading material generation
  - Level-based storytelling

- 📱 Interactive Learning Apps
  - Personalized bedtime stories
  - Moral-based learning games

- 🧒 Personalized Children’s Content
  - Custom birthday stories
  - Therapy storytelling tools
  - Cultural storytelling adaptation

- 📚 Literacy Development Tools
  - Improve reading skills
  - Encourage imagination

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> Input Collection -> Prompt Builder -> GenAI Client -> Gemini API -> Error Handler -> Story Output
```
**Detailed Flow:**
1. **Application Start** - Display welcome message
2. **User Input Collection** - `get_user_input()` collects 5 parameters:
   - Character (hero)
   - Genre
   - Place
   - Main idea/lesson
   - Age group
3. **Prompt Construction** - `create_story_prompt()` builds structured prompt with:
   - Role definition ("professional children's story writer")
   - Story parameters from user input
   - 6-step internal reasoning instructions
   - 4 explicit constraints (vocabulary, tone, length, content)
4. **Client Initialization** - `create_genai_client()` creates authenticated GenAI client
5. **API Call** - `generate_content()` sends prompt to Gemini 3 Flash Preview model
6. **Error Handling** - Catches and handles:
   - AttributeError (invalid response format)
   - ValueError (invalid input)
   - ConnectionError (network issues)
   - TimeoutError (request timeout)
   - Generic Exception (other errors)
7. **Story Output** - Display generated story with visual separators

## ▶️ How to Run the Project

### Step 1: Run Application
```bash
python ai-story-generator.py
```

### Step 2: Provide Story Details
Follow the interactive prompts to enter:
- Main character
- Genre
- Place/setting
- Main idea or lesson
- Target age group

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### 1. Role-Based Prompting
The prompt starts by assigning a specific role to the AI:
```python
"You are a professional children's story writer."
```
**Benefits:**
- Primes the model to adopt appropriate tone and style
- Ensures consistency in narrative voice
- Leverages the model's knowledge of professional storytelling

### 2. Structured Prompting with Parameters
The prompt uses **labeled inputs** to organize information clearly:
```python
Write a {genre} story for children aged {age_group}.
Main Character: {hero}
Place: {place}
Main Idea/Lesson: {idea}
```
**Benefits:**
- Clear separation of input parameters
- Easy to modify individual components
- Reduces ambiguity for the LLM

### 3. Chain-of-Thought Prompting
The prompt includes explicit step-by-step instructions:
```python
Follow these steps internally:
1. Create a magical and engaging setting.
2. Introduce the character with personality traits.
3. Present a small problem or conflict.
4. Show how the character solves the problem.
5. End with a happy resolution.
6. Clearly state the moral starting with 'Moral:'.
```
**Why This Works:**
- Guides the model through narrative structure
- Ensures logical story progression
- Improves coherence and quality
- Guarantees key story elements are included

### 4. Constraint-Based Generation
Explicit constraints control the output:
```python
Constraints:
- Use vocabulary suitable for {age_group}.
- Keep tone positive and warm.
- Story length: 400-500 words.
- Avoid scary or violent elements.
```
**Benefits:**
- Ensures age-appropriate content
- Controls story length
- Maintains safe, positive messaging
- Prevents inappropriate content

### 5. Output Format Specification
The prompt explicitly requests:
- Specific moral statement format: `'Moral:'`
- Clear story structure with beginning, middle, end
- Consistent tone throughout

### Complete Prompt Structure
```python
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
```

### Key Prompt Engineering Principles Applied:
- **Role Assignment**: Sets context and expertise level
- **Structured Input**: Labeled parameters for clarity
- **Chain-of-Thought**: Step-by-step reasoning guide
- **Constraints**: Explicit boundaries for safe output
- **Format Specification**: Clear expectations for structure

## 📌 Sample Output
```powershell
--- Welcome to your AI Magic Storybox!! ---
Please provide details for the story you want to create.
Who is the main character of the story? (e.g., a brave rabbit, a curious child): a brave rabbit
What genre do you want? (e.g., adventure, fantasy, mystery): adventure
Where does the story take place? (e.g., a magical forest, a bustling city): a magical forest
What is the main idea or lesson of the story? (e.g., the importance of kindness, the value of curiosity): value of curiosity
What is the target age group for the story? (e.g., 5-7, 8-10): 5-7

Generating your story...please wait...
------------------------------------------------------------
Once upon a time, in the heart of the Whispering Woods, lived a small rabbit named Barnaby. Barnaby was not like the other rabbits. While his friends were happy munching on ordinary green grass, Barnaby’s long, velvet ears were always twitching for new sounds, and his pink nose was always sniffing for new scents. He wore a tiny yellow vest with a pocket for snacks, and he was known as the bravest bunny in the forest.

The Whispering Woods was a place of wonder. The trees had leaves that shimmered like emeralds, and the flowers hummed sweet lullabies when the wind blew. But there was one part of the forest no one had ever visited: the Great Blue Hill. The older squirrels said it was too far, and the owls said it was too mysterious.

One sunny morning, Barnaby saw a bright, golden butterfly fluttering toward the hill. "I wonder where she is going?" Barnaby whispered to himself. His heart did a little happy dance. He knew he had to follow her.

He hopped over the soft, Mossy Logs and crawled under the Rainbow Arch made of flowers. The further he went, the more beautiful things he saw. He 
found mushrooms that looked like tiny polka-dot umbrellas and pebbles that glowed like stars in the grass. Some animals might have been afraid of 
the unknown, but Barnaby’s curiosity made him feel like an explorer on a grand mission.

Suddenly, he reached a thick wall of tall, purple flowers. They were so tall he couldn't see over them. "What could be on the other side?" he wondered. Instead of turning back to his safe burrow, he gently pushed through the soft, fragrant petals.

Barnaby gasped. On the other side was the most magnificent sight he had ever seen. It was a hidden pond filled with sparkling "Moon-Water" that looked like melted silver. Around the pond grew bushes heavy with "Giggly-Grapes"—fruit that made you let out a tiny, happy giggle every time you took a bite!

Barnaby realized that if he hadn't been curious, he would have spent the whole day just eating plain grass. He stayed a while to play, watching the water-lilies dance. Then, he filled his little vest pocket with Giggly-Grapes to bring home.

When he returned, he shared the grapes with his friends. Soon, the whole forest was filled with the sound of happy giggles. Barnaby led his friends back to the pond, showing them that the world is full of magic if you are just brave enough to look for it.

**Moral: Curiosity leads us to wonderful new discoveries and makes life an exciting adventure.**
```

## ✨ Future Enhancements
- 🖼️ Image Generation Integration
  - Generate illustrations per story scene
- 🎮 Choose-Your-Own-Story Mode
  - Add branching decisions ("Should the rabbit enter the forest or climb the hill")
- 🎤 Voice Narration
  - Convert stories into audio using TTS.
- 🌍 Multilingual Support
  - Generate stories in (Hindi, Spanish, French, Germany)
- 💾 Story Storage System
  - Save stories to database
  - Track reading history
  - User profile
- Add Streamlist Web UI

## 🐛 Troubleshooting
Common Issues:

**API Key Error:**
```python
Error: API key not set or invalid
Solution: Create .env file with GEMINI_API_KEY=your_api_key_here
```

**Connection Error:**
```python
Error: Failed to connect to the API. Check your internet connection.
Solution: Verify your internet connection and try again
```

**Timeout Error:**
```python
Error: Request timed out. Please try again.
Solution: The API took too long to respond. Try again or check API status
```

**Invalid Response Format:**
```python
Error: Invalid response format from the API.
Solution: This is an AttributeError. Try running the script again
```

**Invalid Input Value:**
```python
Invalid input value: [error details]
Solution: Check that all inputs are properly formatted strings
```

**Generic Error:**
```python
An error occurred: [error details]
Solution: Check the error message for specific details and verify your setup
```

## 📝 Configuration Tips

### Prompt Design Guidelines:
- **Be specific:** Use clear task definitions with labeled sections
- **Set constraints:** Define tone, vocabulary, and story length explicitly
- **Request format:** Specify moral statement and story structure
- **Include parameters:** Ask for character, genre, place, lesson, and age group
- **Add moral:** Require a clear moral at the end

### Age Group Selection:
- **5-7:** Simple vocabulary, gentle themes, short sentences
- **8-10:** Slightly more complex language, adventurous plots, deeper lessons

### Model Configuration:
- **gemini-3-flash-preview:** Fast, suitable for interactive story generation
- **No temperature set:** Uses default for balanced creativity and coherence
- Consider adding temperature control for more/less creative stories

### Input Formulation:
- **Be specific:** "A brave rabbit" vs "rabbit"
- **Use proper genres:** "Fantasy" vs "animal story"
- **Single lesson:** Focus on one moral per story for clarity
- **Follow up:** Try new combinations for varied stories



## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your AI story platform

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community

---
## 📝 Happy Story Writing! ✨

Remember: Effective story generation starts with clear inputs and well-designed prompts. Experiment with different tones, characters, and morals to discover what works best for your audience and storytelling goals!
