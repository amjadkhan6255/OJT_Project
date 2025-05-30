import streamlit as st
import random
import os

# Set up page
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💬 Chatbot")
st.markdown("A simple chatbot using if-else logic.")

# Initialize session state to hold chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Type your message...")

# Simple rule-based chatbot response function
def simple_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! 👋"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in message:
        return "Goodbye! 👋"
    elif "name" in message:
        return "I'm your simple chatbot!"
    else:
        return random.choice(["Interesting!", "Tell me more.", "Why do you think that?", "Hmm..."])

# Handle new user input
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("user", user_input))

    # Generate bot response
    response = simple_bot_response(user_input)

    # Add bot response to chat history
    st.session_state.chat_history.append(("bot", response))

# Display chat messages in order
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)