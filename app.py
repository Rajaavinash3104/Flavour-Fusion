import streamlit as st
import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

st.set_page_config(
    page_title="Flavour Fusion",
    page_icon="🍲",
    layout="centered"
)

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API Key not found. Check .env file.")
    st.stop()

genai.configure(api_key=api_key)

# -----------------------------
# Joke Function
# -----------------------------
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

# -----------------------------
# Blog Generation Function
# -----------------------------
def generate_blog(topic, word_count):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    Write a detailed and engaging recipe blog about "{topic}".

    Approximate word count: {word_count}.

    The blog should include:
    - An engaging introduction
    - Ingredients list
    - Step-by-step preparation instructions
    - Tips and variations
    - A short conclusion
    """

    response = model.generate_content(prompt)
    return response.text

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Flavour Fusion 🍲")
st.write("AI-Driven Recipe Blog Generator")

topic = st.text_input("Enter Recipe Topic")
word_count = st.number_input(
    "Enter Desired Word Count",
    min_value=200,
    max_value=2000,
    step=100
)

# Initialize session state
if "blog" not in st.session_state:
    st.session_state.blog = None

# Generate button
if st.button("Generate Blog"):
    if not topic:
        st.warning("Enter a topic.")
    else:
        st.info(get_joke())
        with st.spinner("Generating your recipe blog..."):
            try:
                st.session_state.blog = generate_blog(topic, word_count)
            except Exception:
                st.error("Error generating blog. Please try again.")
                st.stop()

# Display blog if available
if st.session_state.blog:
    st.success("Blog Generated!")
    st.write(st.session_state.blog)

    st.download_button(
        label="Download Blog as Text",
        data=st.session_state.blog,
        file_name="generated_recipe_blog.txt",
        mime="text/plain"
    )