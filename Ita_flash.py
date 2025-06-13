import streamlit as st
import random
import json

# Load JSON data only once
@st.cache_data
def load_data():
    with open("italian_flashcards_2.5flash_5k_true.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Initialize session state
if "remaining_flashcards" not in st.session_state:
    st.session_state.remaining_flashcards = load_data()

if "show_translation" not in st.session_state:
    st.session_state.show_translation = False

if "current_flashcard" not in st.session_state:
    st.session_state.current_flashcard = random.choice(st.session_state.remaining_flashcards)

# Set title
st.title("🇮🇹 Italian Flashcard Practice")

# Show Italian sentence
st.subheader("🗣 Example Sentence in Italian:")
st.markdown(f"**{st.session_state.current_flashcard['example_sentence_native']}**")

# Show translation only if the button was clicked
if st.button("Translate to English"):
    st.session_state.show_translation = True

if st.session_state.show_translation:
    st.subheader("🔁 English Translation:")
    st.markdown(f"**{st.session_state.current_flashcard['example_sentence_english']}**")

# Next sentence button
if st.button("Show another sentence"):
    # Remove the current flashcard from the list
    st.session_state.remaining_flashcards.remove(st.session_state.current_flashcard)

    if not st.session_state.remaining_flashcards:
        st.success("🎉 You've gone through all the flashcards!")
        if st.button("🔄 Restart Flashcards"):
            st.session_state.remaining_flashcards = load_data()
            st.session_state.current_flashcard = random.choice(st.session_state.remaining_flashcards)
            st.session_state.show_translation = False
    else:
        # Get a new flashcard
        st.session_state.current_flashcard = random.choice(st.session_state.remaining_flashcards)
        st.session_state.show_translation = False

