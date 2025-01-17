import streamlit as st
import requests

st.title("Educational Chatbot")
st.write("Ask me educational questions or interact with me!")

user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )
        for msg in response.json():
            st.text_area("Bot:", value=msg['text'], height=100)
