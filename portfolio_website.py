import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hej :wave:")
    st.title("Ja sam Tonci")

with col2:
    st.image("images/Stream.jpg")

st.write(" ")
st.title("Moj bot")
# st.write("Pitaj me...")
user_question = st.text_input("Pitaj me...")
if st.button("POSALJI", use_container_width=400):
    # prompt = user_question
    prompt = persona + "Here is the user_question: "+ user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.write(" ")
st.write(" ")
col1, col2 = st.columns(2)
with col1:
    st.subheader("YT Channel ")
    st.write("Najbolji IKT kanal u Dalmaciji i šire! ")

with col2:
    st.video("https://www.youtube.com/watch?v=QTcNnXMgJTo&list=PLRXnG4Gb6CEJrxCVbGtWRoX0IFXRD2wvz")

st.write(" ")
st.title("Moj setup")
st.image("images/Setup.jpg")

st.write(" ")
st.title("Moje vjestine")
st.slider("Programiranje", 0, 100, 60)
st.slider("Trening", 0, 100, 90)
st.slider("Storytelling", 0, 100, 50)

st.file_uploader("Upload datoteku")

st.write(" ")
st.title("Galerija")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/01.png")
with col2:
    st.image("images/02.png")
with col3:
    st.image("images/03.png")

st.write(" ")
st.write(" ")
st.write("KONTAKT")
st.title("Za upite, pls posaljite mi mejl")
st.subheader("tonci.kaleb@gmail.com")