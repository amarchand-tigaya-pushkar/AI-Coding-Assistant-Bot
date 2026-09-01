# 💻 AI Coding Assistant Bot

An AI-powered coding assistant built using **Python, LangChain, OpenAI API, and Streamlit**. The project is designed to help beginners generate, explain, debug, and convert programming logic into code.

## 🎯 Project Objective

This project can:

- Generate Python code
- Explain code
- Debug code
- Convert logic into code
- Provide beginner-friendly programming help

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- LangChain OpenAI
- OpenAI API
- python-dotenv

## ✨ Features

### Programming Language Selection

The application supports:

- Python
- Java
- C
- C++
- JavaScript

### Task Types

Users can select:

- Generate Code
- Explain Code
- Debug Code
- Convert Logic to Code
- Create Mini Project

### AI Response

The bot is designed to provide:

1. Short explanation
2. Complete code with comments
3. Output example
4. Beginner notes

## 🔄 How It Works

```text
User enters coding question
        ↓
Streamlit takes input
        ↓
LangChain creates prompt
        ↓
OpenAI model generates answer
        ↓
Bot displays code and explanation
```

## 📁 Project Structure

```text
AI-Coding-Assistant-Bot/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The `.env` file containing the OpenAI API key should remain local and must not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Coding-Assistant-Bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Configure OpenAI API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Never publish or share your API key publicly.

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Example Questions

Try questions such as:

```text
Write Python code to add two numbers.
```

```text
Create a calculator using Python.
```

```text
Explain this code: for i in range(5): print(i)
```

```text
Debug this code: print("Hello World"
```

```text
Create a student marks management mini project.
```

## 🧩 Testing Examples

### Example 1 — Even or Odd

```text
Write Python code to check even or odd number.
```

The bot generates Python code that takes a number as input and checks whether it is even or odd.

### Example 2 — Simple Calculator

```text
Create Python code for simple calculator.
```

The bot generates calculator code.

### Example 3 — Debugging

```text
Debug this code: print("Hello World"
```

The bot explains the missing bracket and provides the corrected code.

## 📌 Project Analysis

This project uses:

- **Streamlit** for the web interface
- **LangChain** for prompt handling
- **OpenAI model** for code generation
- **Python** for backend logic

The user enters a coding problem, selects a programming language and task type, and the bot generates code with comments.

## 🐛 Common Errors

### API key not found

Check that `.env` contains:

```env
OPENAI_API_KEY=your_api_key_here
```

### Streamlit command not found

Install Streamlit:

```bash
pip install streamlit
```

### langchain_openai not found

Install:

```bash
pip install langchain-openai
```

## 📄 Resume / CV Title

**AI Coding Assistant Bot Using LangChain for Automated Code Generation**

## 📝 Project Description

Developed an AI Coding Assistant Bot using Python, LangChain, OpenAI API, and Streamlit to generate, explain, and debug programming code for beginners.

## 👨‍💻 Author

**Amarchand Tigaya Pushkar**
