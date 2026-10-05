import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Check API key
if not API_KEY:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()

# Gemini client
client = genai.Client(api_key=API_KEY)

# Page settings
st.set_page_config(
    page_title="AI Coding Assistant",
    page_icon="💻",
    layout="wide"
)

# Title
st.title("💻 AI Coding Assistant for Students")
st.write("Learn coding, generate programs, debug errors and understand code easily.")

# Sidebar
with st.sidebar:

    st.header("⚙️ Settings")

    language = st.selectbox(
        "Select Programming Language",
        [
            "Python",
            "C",
            "C++",
            "Java",
            "JavaScript",
            "SQL"
        ]
    )

    task = st.selectbox(
        "Select Task",
        [
            "Generate Code",
            "Explain Code",
            "Debug Code",
            "Improve Code",
            "Solve Coding Problem",
            "Generate Test Cases"
        ]
    )

# Question
st.subheader("📝 Coding Question")

question = st.text_area(
    "Enter your coding question:",
    placeholder="Example: Write a Python program to check whether a number is prime.",
    height=150
)

# Code
st.subheader("💻 Your Code")

code = st.text_area(
    "Paste your code here (optional):",
    placeholder="Paste your code here...",
    height=250
)

# Ask button
if st.button("🚀 Ask AI", use_container_width=True):

    if not question.strip() and not code.strip():
        st.warning("Please enter a question or code.")
        st.stop()

    # AI prompt
    prompt = f"""
You are an AI Coding Assistant for college students.

Programming Language:
{language}

Task:
{task}

Student Question:
{question}

Student Code:
{code}

Give a simple and beginner-friendly answer.

Follow these instructions:

1. Explain the answer clearly.
2. Use simple language suitable for students.
3. If code is required, provide complete working code.
4. If the student's code contains errors, identify the errors.
5. Provide corrected code when necessary.
6. Explain the important parts of the code.
7. Give sample input and output when useful.
8. Give time complexity when appropriate.
9. Do not make the solution unnecessarily complicated.
"""

    # Call Gemini
    with st.spinner("🤖 AI is generating your answer..."):

        try:

            response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
)

            answer = response.text

            st.subheader("🤖 AI Answer")
            st.markdown(answer)

        except Exception as e:

            st.error(f"Something went wrong: {e}")


# Footer
st.divider()

st.caption(
    "AI Coding Assistant for Students | Python + Streamlit + Gemini"
)