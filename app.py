# -------------------------------------------------
# AI Coding Assistant Bot
# Using LangChain, OpenAI, Python, and Streamlit
# -------------------------------------------------
# Import required libraries
import streamlit as st
from dotenv import load_dotenv
import os
# Import LangChain Groq chat model
from langchain_groq import ChatGroq
# Import prompt template
from langchain_core.prompts import ChatPromptTemplate
# -------------------------------------------------
# Load API key from .env file
# -------------------------------------------------
load_dotenv()
# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")
# -------------------------------------------------
# Streamlit page setting
# -------------------------------------------------
st.set_page_config(
 page_title="AI Coding Assistant Bot",
 page_icon="💻",
 layout="centered"
)
# -------------------------------------------------
# App title
# -------------------------------------------------
st.title("💻 AI Coding Assistant Bot")
st.write(
 "This bot helps beginners generate, explain, and debug code using LangChain."
)
# -------------------------------------------------
# Check API key
# -------------------------------------------------
if not api_key:
 st.error("Groq API key not found. Please add GROQ_API_KEY in .env file.")
 st.stop()
# -------------------------------------------------
# Create LLM model
# -------------------------------------------------
llm = ChatGroq(
 model="openai/gpt-oss-120b",
 temperature=0.2
)
# -------------------------------------------------
# Create prompt template
# -------------------------------------------------
prompt = ChatPromptTemplate.from_messages([
 (
 "system",
 """
 You are an AI Coding Assistant for absolute beginners.
 Give simple, correct, and well-commented code.
 Explain every step in easy language.
 Avoid advanced concepts unless needed.
 """
 ),
 (
 "human",
 """
 User request:
 {user_question}
 Programming language:
 {language}
 Task type:
 {task_type}
 Give:
 1. Short explanation
 2. Complete code with comments
 3. Output example
 4. Beginner notes
 """
 )
])
# -------------------------------------------------
# User input section
# -------------------------------------------------
language = st.selectbox(
 "Choose Programming Language",
 ["Python", "Java", "C", "C++", "JavaScript"]
)
task_type = st.selectbox(
 "Choose Task Type",
 [
 "Generate Code",
 "Explain Code",
 "Debug Code",
 "Convert Logic to Code",
 "Create Mini Project"
 ]
)
user_question = st.text_area(
 "Enter your coding question:",
 placeholder="Example: Write Python code to check whether a number is even or odd"
)
# -------------------------------------------------
# Generate button
# -------------------------------------------------
if st.button("Generate Answer"):
 # Check empty input
 if user_question.strip() == "":
  st.warning("Please enter your coding question.")
else:
 with st.spinner("Generating answer..."):
 # Format final prompt
  final_prompt = prompt.format_messages(
   user_question=user_question,
   language=language,
   task_type=task_type
 )
 # Send prompt to LLM
 response = llm.invoke(final_prompt)
 # Display AI response
 st.subheader("AI Response")
 st.write(response.content)
# -------------------------------------------------
# Example questions
# -------------------------------------------------
st.info("""
1. Write Python code to add two numbers.
2. Create a calculator using Python.
3. Explain this code: for i in range(5): print(i)
4. Debug this code: print("Hello World"
5. Create a student marks management mini project.
""")