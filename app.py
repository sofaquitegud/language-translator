import streamlit as st
from translatepy import Translator


def translate_text(text, target_language="ms"):
    translator = Translator()
    try:
        translated = translator.translate(text, target_language)

        return translated.result

    except Exception as e:

        return f"Error during translation: {str(e)}"


# Streamlit interface
st.title("English to BM Translator")

st.write("Paste your text below:")

# Input text area
input_text = st.text_area("Input Text", placeholder="Type or paste your text here...")

# Translate button
if st.button("Translate"):
    if input_text.strip():
        # Perform translation synchronously
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text)

            # Display result
            st.subheader("Translated Text:")
            st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.markdown("*Prototype created for translating English text to BM.*")
