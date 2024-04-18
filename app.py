import streamlit as st
import google.generativeai as genai

st.title("AI chatbot with Google GenAI")

f = open("keys/Gemini_api_key.txt")
key = f.read()
genai.configure(api_key=key)


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""you are a helpful AI teaching Assistant.
                              
                              Given a data science topic help the user understand it. You also answer any followup quetions as well. If a question is not related to data science, the response should be 'that is beyond my knowledge.'""")


if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response=chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"]=chat.history