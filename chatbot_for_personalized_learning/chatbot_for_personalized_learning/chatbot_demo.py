import streamlit as st
import requests

# Set up Streamlit app title and description
st.title("Chatbot Demo")
st.write("This is a demo application to interact with the Rasa chatbot.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to send a message to the Rasa server and get a response
def send_message_to_rasa(message):
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL
    try:
        response = requests.post(rasa_url, json={"sender": "user", "message": message})
        if response.status_code == 200:
            return response.json()
        else:
            return [{"text": "Error: Unable to reach the Rasa server."}]
    except Exception as e:
        return [{"text": f"Error: {str(e)}"}]

# Input text box for user messages
user_message = st.text_input("You:", placeholder="Type your message here...")

# Display chat history
for msg in st.session_state["messages"]:
    if msg["sender"] == "user":
        st.write(f"**You**: {msg['text']}")
    else:
        st.write(f"**Bot**: {msg['text']}")

# Process user input
if st.button("Send") and user_message.strip():
    # Append user message to chat history
    st.session_state["messages"].append({"sender": "user", "text": user_message.strip()})

    # Get the chatbot's response
    responses = send_message_to_rasa(user_message.strip())
    for response in responses:
        st.session_state["messages"].append({"sender": "bot", "text": response.get("text", "")})

    # Clear the input box (set value to empty string)
    user_message = ""
