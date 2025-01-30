import streamlit as st
from translate import translate_text

st.title("AI-Powered English to Malay Translator")

st.write("Paste your English text below:")

input_text = st.text_area("Input text", placeholder="Type or paste your text here...")

# Model selection dropdown
model_options = {
    "Mistral 7B Instruct": "mistralai/mistral-7b-instruct",
    "GPT-4 Turbo": "openai/gpt-4-turbo",
    "Llama 3 70B": "meta-llama/llama-3-70b-instruct",
    "Command R+": "cohere/command-r-plus",
}

selected_model = st.selectbox(
    "Select a translation model:", options=list(model_options.keys())
)

if st.button("Translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            # Call the translate_text function with the selected model
            translated_text = translate_text(
                input_text, model=model_options[selected_model]
            )
            st.subheader("Translated Text:")
            st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")

st.markdown("---")
st.markdown("*Prototype using OpenRouter's AI models.*")
