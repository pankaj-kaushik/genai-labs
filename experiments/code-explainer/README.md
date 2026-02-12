# 📝 AI Email / Message Writer (Gemini LLM)

An AI-powered Code Explainer built using **Python** and **Google Gemini LLM**.  
This tool helps users by explaining python code in simple, human-readable language using Large Language Models (LLMs).


This project helps learners quickly understand complex code in simple terms.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from complex code

## 🚀 What This Project Does
- Read code from file
- Generate a detailed explanation of what the code does
- Explains logic flow, functions and key components
- Identify Time and Space Complexity
- Suggest Improvements or Refactoring Areas

The system sends the provided code to an LLM (e.g., OpenAI, Gemini, Anthropic) and returns a structured explanation in easy-to-understand language.

## 🎯 Learning Outcomes
- How GenAI APIs work
- Prompt Engineering Basics
- Secure API key handling
- Real-world GenAI use cases
- End-to-end AI application flow

## 🧩 Use Cases
- Understanding complex code
- Understanding legacy codebase
- Reviewing unfamiliar codebases
- Creating simplified explanations
- Generating teaching material
- Document generation
- Refactoring suggestions

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd code-explainer
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
⚠️ Never commit .env to GitHub.

## ▶️ How to Run the 
### Step 1: Update ```code.py``` file under ```data``` directory.
Copy and paste your code in ```code.py``` file.

### Step 2:  Run main.py
```bash
python main.py
```

## 🧠 Prompt Engineering Used
We have used following prompt techniques to ensure AI behaves reliably. Here is the breakdown.

### Zero-Shot Prompting
In `create_user_prompt()` method we passed the instruction in `user_prompt` (see below) but didn't mention any specific examples. The code tells the AI **what** to do (Analyze this Python code and provide the requested sections.) and **instructions** to generate required information, but it gives zero finished examples of a "good" code explanation for the AI to copy. It relies entirely on the AI's pre-existing knowledge of what a good explanation looks like.

### Structured Prompting
In `create_user_prompt()` method, we enclose the user's code (see below) in triple backticks (```python {content}```) to clearly separate **instructions** from **data**. This prevents prompt injection attacks where the model might misinterpret user code as commands.

```python
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
```

### Role Prompting
In ```explain_code()``` we set ```system_instruction```` (see below) to force a specialist role (e.g., "Senior Developer"), priming the model’s tone, vocabulary, and perspective before it analyzes the code.

```python
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
```
## 📌 Sample Output
```powershell
--- Welcome to your AI Code Explainer! ---
Analyzing code from file: data/code.py
Creating Gen AI client...
Explaining code... Please wait.

------------------------------------------------------------
This is a clean and well-optimized implementation of the **Bubble Sort** algorithm in Python. Below is a detailed analysis from a Senior Developer's perspective.

### 1. Overview
The code implements the Bubble Sort algorithm, a comparison-based sorting method. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order (ascending in this case). The "bubble" name comes from the way larger elements "bubble" up to 
their correct positions at the end of the list with each iteration.

### 2. Key Components and Logic
*   **The Outer Loop (`for i in range(n)`):** This loop ensures that the process is repeated enough times to sort the entire list. In the worst case, it takes $n$ passes to sort $n$ elements.
*   **The Inner Loop (`for j in range(0, n - i - 1)`):**
    *   This loop performs the actual comparisons.
    *   **Optimization:** The range `n - i - 1` is an optimization. After each pass of the outer loop, the largest element of the unsorted portion is guaranteed to be at its final sorted position. Therefore, we don't need to check the last `i` elements.
*   **The Swap Logic (`arr[j], arr[j + 1] = arr[j + 1], arr[j]`):** This uses Python’s idiomatic tuple unpacking to swap two variables without needing a temporary third variable.
*   **The Early Exit Optimization (`swapped` flag):** This is a crucial optimization. If the inner loop completes without making a single swap, it means the array is already sorted. The `break` statement terminates the function early, preventing unnecessary iterations.

### 3. Potential Issues and Improvements

#### Issues:
*   **In-place Mutation:** The function modifies the original list passed to it (`arr`) and also returns it. In Python, it is standard practice to either modify in-place and return `None` (like `list.sort()`) or return a new sorted list and leave the original untouched (like `sorted()`). Returning the modified list can sometimes lead to confusion about whether a copy was made.
*   **Type Hinting:** For modern Python (3.9+), adding type hints would improve readability and IDE support.

#### Improvements:
*   **Type Hints:**
    ```python
    from typing import List, Any

    def bubble_sort(arr: List[Any]) -> List[Any]:
        # ... logic ...
    ```
*   **Algorithm Choice:** While this is a great educational example, Bubble Sort is rarely used in production. Python’s built-in `list.sort()` and `sorted()` use **Timsort**, which is significantly faster ($O(n \log n)$) and handles real-world data patterns much more efficiently.

### 4. Time and Space Complexity Analysis

#### Time Complexity:
*   **Best Case: $O(n)$**
    This occurs when the input list is already sorted. The inner loop runs once, no swaps are made, the `swapped` flag remains `False`, and the function breaks.
*   **Average Case: $O(n^2)$**
    On average, the number of comparisons and swaps grows quadratically with the size of the input.
*   **Worst Case: $O(n^2)$**
    This occurs when the input list is sorted in reverse order. Every possible comparison results in a swap.

#### Space Complexity:
*   **Space: $O(1)$ (Constant Space)**
    The algorithm is "in-place." It does not require additional memory proportional to the input size; it only uses a few variables (`n`, `i`, `j`, `swapped`) regardless of how large the list is.

### Summary
This is a **"Best-in-Class" implementation of Bubble Sort**. It includes the two standard optimizations (reducing the inner loop range and the early-exit flag) that elevate it above a naive implementation. It is stable (preserves the order of equal elements) and memory-efficient, though limited by its $O(n^2)$ time complexity.
------------------------------------------------------------
```
## ✨ Future Enhancements
- Multi-Language Support: Expand beyond Python to explain C++, Java and Rust
- Multi-Mode Explanation (Beginner/Intermediate/Expert Mode)
- Interactive Q & A (A chat mode where you can ask follow-up questions about specific functions) 
- Add Streamlit web UI (A browser-based interface for drag and drop file uploads)
- Export to PDF/Markdown (Save the AI-generated report as a standalone documentation file.)
- Code Visualization (Generate Flowcharts, Sequence Diagrams & Execution Flow)

## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community