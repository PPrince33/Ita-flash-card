import streamlit as st
import random
import json

# Load JSON data
@st.cache_data
def load_data():
    with open("italian_flashcards_2.5flash_5k_true.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

# Pick a random flashcard
if "current_index" not in st.session_state:
    st.session_state.current_index = random.randint(0, len(data) - 1)

flashcard = data[st.session_state.current_index]

# Title
st.title("🇮🇹 Italian Flashcard Practice")

# Show the Italian sentence
st.subheader("🗣 Example Sentence in Italian:")
st.markdown(f"**{flashcard['example_sentence_native']}**")

# Button to show the English translation
if st.button("Translate to English"):
    st.subheader("🔁 English Translation:")
    st.markdown(f"**{flashcard['example_sentence_english']}**")

# Option to move to a new random sentence
if st.button("Show another sentence"):
    st.session_state.current_index = random.randint(0, len(data) - 1)
    st.experimental_rerun()
