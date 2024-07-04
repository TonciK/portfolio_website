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

persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 
        
        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """

st.title("Moj bot")
# st.write("Pitaj me...")
user_question = st.text_input("Pitaj me o Murtazi personi...")
if st.button("POSALJI", use_container_width=400):
    prompt = persona +"Here is the user_question: "+ user_question
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
