import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="T5 Translator", layout="centered")

st.title("🌍 T5 English to French Translator")

# Load model only once using session state
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="t5-small")

model = load_model()

# User input
text_input = st.text_area("Enter English text to translate:", height=100)

if st.button("Translate"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_text = f"translate English to French: {text_input}"
        output = model(input_text, max_length=50, num_return_sequences=1)
        translated_text = output[0]['generated_text']
        st.success(f"🇫🇷 Translation: {translated_text}")
