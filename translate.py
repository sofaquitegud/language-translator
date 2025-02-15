from urllib import response
import requests
import os
import time

# Load OpenRouter API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


def translate_text(text, model):
    """
    Translate English text to BM using specified model on OpenRouter
    """
    if not API_KEY:
        return "Error: API key is missing. Please set your OpenRouter API key."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://language-translator-cjsg5laxbtpccxoovujisa.streamlit.app/",
    }

    # Refined system prompt for better translations
    system_prompt = (
        "You are an expert Malay linguist and translator. Translate the following English text into **fluent, natural, and idiomatic Bahasa Malaysia**, ensuring that:\n"
        "1. The translation **flows naturally**, as if originally written in Malay.\n"
        "2. Sentence structure follows **Malay grammar rules** and avoids direct AI-literal translations.\n"
        "3. Use **appropriate Malay idioms or phrases** where suitable to enhance readability.\n"
        "4. Ensure a **formal yet conversational tone** suitable for blog articles or professional documents.\n\n"
        "Now, translate the following text:"
    )

    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
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

        # Print the full response for debugging
        print("Full API Response:", response.json())

        # Check if the response contains the expected keys
        if "choices" in response.json():
            return response.json()["choices"][0]["message"]["content"]
        else:
            return (
                f"Error: Unexpected API response structure. Response: {response.json()}"
            )

    except requests.exceptions.RequestException as e:
        return f"Error during translation: {str(e)}"
    finally:
        # Add a 1-second delay between requests to avoid rate limits
        time.sleep(1)
