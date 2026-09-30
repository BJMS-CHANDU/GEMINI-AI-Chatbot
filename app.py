import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

if not api_key:
    st.error("GEMINI_API_KEY was not found in your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #14152f, #3d348b);
}

h1 {
    color: white !important;
    text-align: center;
}

.stTextArea label {
    color: white !important;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: white !important;
    color: black !important;
    border: 2px solid #7777ff !important;
    border-radius: 15px !important;
}

.stButton button {
    background: linear-gradient(90deg, #00b4db, #9b4dff) !important;
    color: white !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 12px 25px !important;
    font-size: 16px !important;
}

.response-box {
    background-color: white;
    color: black !important;
    padding: 25px;
    border-radius: 25px;
    margin-top: 30px;
    border-left: 7px solid #7777ff;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.25);
    font-size: 17px;
    line-height: 1.7;
}

.response-box * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini Anything!")

prompt = st.text_area(
    "Enter your question:",
    height=150,
    placeholder="Type your question here..."
)

if st.button("🚀 Generate Response"):

    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            answer = response.text

            st.markdown(
                f"""
                <div class="response-box">
                    {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")