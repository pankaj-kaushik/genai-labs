# 📘 AI Study Buddy / Concept Explainer (Gemini LLM)

An AI-powered **Study Buddy** built using **Python** and **Google Gemini LLM** that explains complex concepts in **simple, beginner-friendly language** using real-life analogies and examples.

This project helps learners quickly understand difficult topics without technical jargon.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from long articles

## 🚀 What This Project Does
- Enter any topic or concept
- Get simplified explanations
- Understand using real-life analogies
- Learn faster with beginner-friendly examples

## 🎯 Learning Outcomes
- How GenAI APIs work
- Prompt engineering basics
- Secure API key handling
- Real-world GenAI use cases
- End-to-end AI application flow

## 🧩 Use Cases
- Students learning new subjects  
- Software engineers learning new technologies  
- Interview preparation  
- Quick concept revision  
- Self-learning and curiosity-based exploration

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd study-buddy
```
### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```
Activate it:

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Get Gemini API Key
- Visit Google AI Studio (https://aistudio.google.com/api-keys)
- Create a new API Key
- Copy the key

### Step 5: Create .env File
- Create a file named ```.env``` in the root directory and update the Gemini API Key
- Note: You can use ```.env.example``` file and rename it to ```.env```
- ⚠️ Never commit .env to GitHub.

## ▶️ How to Run the Project
### Run main.py
```bash
python main.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques in the code below to ensure AI behaves reliably. Here is the breakdown.

- **Role prompt:** `"You are an expert Study Buddy."` sets the assistant's persona, tone, and expected behavior.
- **Instruction-style prompts:** The `Task:`, `Constraints:`, and `Format:` lines give concrete instructions, output constraints, and structure for the response.
- **Combined effect:** Persona + explicit instructions produce focused, consistent, and well-formatted explanations.

```python
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
```


## 📌 Sample Output
```powershell
--- Welcome to your AI Study Buddy! ---
Please enter the detiails of the topic you want to learn about.
------------------------------------------------------------
What concept would you like to learn today? Array
What is your learning level? (Beginner/Intermediate/Advanced) Beginner

Creating prompt...       

Creating Gen AI client...

Analyzing 'Array'... Please wait.

------------------------------------------------------------
Hey there! I'm your **Study Buddy**, and today we are going to talk about **Arrays**. 

Don't let the name scare you—it’s actually a very simple way to keep things organized.

---

### 📦 The Big Idea: The "Magic Toy Shelf"

Imagine you have a bunch of cool action figures. If you throw them all into a big messy toy box, it’s hard to find the one you want, right?

An **Array** is like a **long, straight shelf** where every toy has its own exact spot.

### 🚗 Why use an Array?

Think of a **train**. Each car on the train is hooked to the next one in a perfect line.

*   **It’s Organized:** You know exactly where the first car is, the second car is, and the last car is.
*   **It’s Fast:** If I tell you, "Go to the 3rd car," you don't have to search the whole train; you just count to three!

### 🔢 The "Golden Rule" of Arrays (The Zero Rule)

This is the only tricky part about arrays. In the human world, we usually start counting at **1**. But in the computer world, **computers always start counting at 0.**

Imagine your toy shelf again:
*   The **1st** toy is at spot **0**.
*   The **2nd** toy is at spot **1**.
*   The **3rd** toy is at spot **2**.

It sounds weird, but it's like the ground floor of a building. Sometimes the ground floor is "0," and the next floor up is "1."

### 📝 Three Things to Remember about Arrays:

1.  **They Like "Same-Sized" Things:** Usually, an array likes to hold the same kind of stuff. Imagine a carton of eggs—it's built for eggs, not an egg, then a shoe, then a sandwich.
2.  **They Stay in Order:** If you put your Red Power Ranger in the first spot, he stays there unless you move him. He won't wander off!
3.  **They Have a Limit:** When you build a shelf with 5 spots, it stays 5 spots big. To add a 6th toy, you’d usually need a bigger shelf!

### 🌟 Summary
An **Array** is just a **numbered list** of items sitting side-by-side.

*   **The Items:** The toys on the shelf.
*   **The Index:** The number written on the shelf (starting at 0!) that tells you where the toy is.

**Does that make sense, or should we try another analogy?** 🧩
------------------------------------------------------------
```

## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community