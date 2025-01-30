import streamlit as st
from translate import translate_text

st.title("AI-Powered English to Malay Translator")

st.write("Paste your English text below:")

input_text = st.text_area("Input text", placeholder="Type or paste your text here...")

if st.button("Translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text)
            st.subheader("Translated Text:")
            st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")

st.markdown("---")
st.markdown("*Prototype using OpenRouter's Gemini Flash 1.5 8b Model.*")
