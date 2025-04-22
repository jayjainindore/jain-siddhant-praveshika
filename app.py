
import streamlit as st
import pandas as pd
import difflib

# Load Google Sheet as public CSV
sheet_url = "https://docs.google.com/spreadsheets/d/1iVLc1UTIVMkEPa8TEiEmmuxp8q5-4FZ9W0MkAQbfVNA/export?format=csv&gid=0"
df = pd.read_csv(sheet_url)

# Ensure column names
df.columns = [col.strip() for col in df.columns]
questions = df["Questions(Hindi)"].fillna("").tolist()
answers = df["Answer(Hindi)"].fillna("").tolist()
qa_pairs = dict(zip(questions, answers))

# Function to find best match
@st.cache_data
def get_best_answer(user_input):
    matches = difflib.get_close_matches(user_input, qa_pairs.keys(), n=1, cutoff=0.5)
    if matches:
        return qa_pairs[matches[0]]
    else:
        return "क्षमा करें, मैं आपके प्रश्न का उत्तर नहीं पा रहा हूँ."

# Streamlit UI
st.title("🔍 हिंदी प्रश्नोत्तरी (Praveshika)")
st.markdown("नीचे अपना प्रश्न लिखें और उत्तर प्राप्त करें:")

user_question = st.text_input("प्रश्न दर्ज करें:")

if user_question:
    answer = get_best_answer(user_question)
    st.markdown(f"**उत्तर:** {answer}")
