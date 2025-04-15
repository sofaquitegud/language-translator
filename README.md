# AI-Powered Malay to Jawi Translator

## Overview

This project is an AI-powered translation tool that automatically translates Malay text into Jawi. It uses advanced AI models to provide fluent, natural, and idiomatic translations, tailored to ensure the output fits the tone and context of formal and conversational Malay.

## Features

1. Translate Malay text to Jawi using AI models.
2. Model selection: Users can choose from various AI models to generate translations.
3. Refined translation: The translations are tailored for fluency, naturalness, and grammatical correctness in BM.
4. User-friendly interface: Simple web interface built using Streamlit.

## Models Supported

1. GPT-4 Turbo
2. Mistral 7B Instruct
3. Command R+
4. Llama 3 70B

These models can be selected in the app to customize the translation output.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:

```
git clone https://github.com/sofaquitegud/language-translator.git
cd language-translator
```

2. Install required dependencies:

- Use pip to install the required Python libraries:

```
pip install -r requirements.txt
```

3. Set up environment variables:
   Create a .env file and add your API key for OpenRouter:

```
OPENROUTER_API_KEY=your_api_key_here
```

4. Run the app:

- Start the Streamlit app

```
streamlit run app.py
```

Open the provided local link in your browser to use the app.

## Usage

1. Enter English text in the input box.
2. Select a translation model from the dropdown menu.
3. Click "Translate" to get the translation in Bahasa Malaysia.
4. Review the translation and try using different models for varying results.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. We welcome any improvements to the translation quality, features, or user interface.

## License

This project is open-source and available under the MIT License.
