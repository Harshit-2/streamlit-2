import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    st.title("Chatbot Web App")

    user_input = st.text_input("Enter your message here:")
    if st.button("Send"):
        if user_input:
            output = query({"inputs": user_input})
            st.write("Bot:", output['generated_text'])
        else:
            st.write("Please enter a message.")

if __name__ == "__main__":
    main()
