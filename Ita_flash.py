import streamlit as st
import random
import json

# Load JSON data
@st.cache_data
def load_data():
    with open("italian_flashcards_2.5flash_5k_true.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

# Session state to store current flashcard index
if "current_index" not in st.session_state:
    st.session_state.current_index = random.randint(0, len(data) - 1)

flashcard = data[st.session_state.current_index]

st.title("🇮🇹 Italian Flashcard Practice")

st.subheader("🗣 Example Sentence in Italian:")
st.markdown(f"**{flashcard['example_sentence_native']}**")

# Button to show translation
if st.button("Translate to English"):
    st.subheader("🔁 English Translation:")
    st.markdown(f"**{flashcard['example_sentence_english']}**")

# Button to get a new random flashcard
if st.button("Show another sentence"):
    st.session_state.current_index = random.randint(0, len(data) - 1)
    st.experimental_rerun()  # ✅ This is allowed here

