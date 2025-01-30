from urllib import response
import requests
import os

# Load OpenRouter API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


def translate_text(text):
    """
    Translate English text to BM using Gemini Flash 1.5 8B model
    """
    if not API_KEY:
        return "Error: API key is missing. Please set your OpenRouter API key in environment variables."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://language-translator-cjsg5laxbtpccxoovujisa.streamlit.app/",
    }

    data = {
        "model": "google/gemini-flash-1.5-8b",
        "messages": [
            {
                "role": "system",
                "content": "Translate the following English text into fluent and natural Malay.",
            },
            {"role": "user", "content": text},
        ],
        "temperature": 0.5,
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data
        )
        # Raise an error if request fails
        response.raise_for_status()
        return response.json()["choices"][0]["messages"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error during translation: {str(e)}"
