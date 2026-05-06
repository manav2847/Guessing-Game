import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")
st.title("🎯 The Ultimate Guessing Game")

# Sidebar for settings
with st.sidebar:
    st.header("Game Settings")
    lower = st.number_input("Lower Bound", value=1)
    upper = st.number_input("Upper Bound", value=100)
    chances = st.number_input("Total Chances", value=7)
    
    if st.button("Reset Game"):
        st.session_state.secret_number = random.randint(lower, upper)
        st.session_state.attempts = 0
        st.session_state.game_over = False

# Initialize the random number if it doesn't exist
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(lower, upper)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game UI
if not st.session_state.game_over:
    guess = st.number_input(f"Guess a number between {lower} and {upper}:", min_value=lower, max_value=upper)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Correct! You won in {st.session_state.attempts} tries!")
            st.session_state.game_over = True
        elif st.session_state.attempts >= chances:
            st.error(f"💀 Game Over! The number was {st.session_state.secret_number}.")
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.info("Hint: The number is HIGHER!")
        else:
            st.info("Hint: The number is LOWER!")

st.write(f"Attempts Used: {st.session_state.attempts} / {chances}")
