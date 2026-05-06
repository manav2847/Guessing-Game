import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Setup range and chances
lower = st.sidebar.number_input("Lower Bound", value=1)
upper = st.sidebar.number_input("Upper Bound", value=100)
chances = st.sidebar.number_input("Total Chances", value=7)

# Initialize game state
if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(lower, upper)
    st.session_state.attempts = 0

# Game logic
guess = st.number_input("Enter your guess:", min_value=lower, max_value=upper)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess == st.session_state.secret:
        st.success(f"Winner! It was {guess}!")
        if st.button("Play Again"):
            del st.session_state.secret
    elif st.session_state.attempts >= chances:
        st.error(f"Game Over! The number was {st.session_state.secret}")
    elif guess < st.session_state.secret:
        st.info("Higher!")
    else:
        st.info("Lower!")
       
            
