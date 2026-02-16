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
After completing this project, you will understand
- 🧩 How to design **structured prompts**
- 🧠 How to guide **LLM reasoning** step-by-step
- 🎛️ How to control **creativity** with constraints
- 🔐 How to integrate **Gemini API with Python**
- 📏 How to manage **output format** and tone
- 🛡️ How to design **safe AI** content for kids
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
User -> CLI/Web Interface -> Collect User Inputs -> Prompt Builder -> Gemini LLM API -> Response Processor -> Formatted Output to User
```
1. Read user inputs through CLI
2. System builds a structured prompt using user inputs
3. Prompt is sent to Gemini LLM API
4. Gemini analyzes prompt and generates response
5. Application processes and formats response
6. Output displayed to user

## ▶️ How to Run the Project
### Step 1: Run Application
```bash
python gemini-story-generator.py
```
## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Structured Prompting
In the `create-story-prompt()` method, we passed the instruction in `user_prompt` (see below) that dictate the organization of the input and the exact layout of the output.
Instead of writing a long, conversational sentence, we used **labels** and **delimiters** to organize the information.

### Chain-of-Thought Prompting
In the `create-story-prompt()` method, we instruct the model to internally
- Build Setting
- Introduce Character
- Add conflict
- Create resolution
- State - moral
This improves coherence and story quality.

```python
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
```
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

## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your AI story platform

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community