from urllib import response
import requests
import os
import time

# Load OpenRouter API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


def translate_text(text, model):
    """
    Translate Malay text to Jawi using specified model.
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
        "You are an expert Malay linguist specializing in Jawi script. Convert the following Malay text written in Rumi to **accurate and natural Jawi script**, ensuring that:\n"
        "1. The conversion follows **standard Jawi orthography** as commonly used in Malaysia.\n"
        "2. Maintain correct **spelling conventions** for loanwords and native Malay terms.\n"
        "3. Ensure readability and correctness based on **Dewan Bahasa dan Pustaka (DBP) guidelines**.\n"
        "4. Avoid direct AI-literal transliteration errors by considering proper Jawi equivalents.\n\n"
        "Now, convert the following Rumi text to Jawi:"
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
