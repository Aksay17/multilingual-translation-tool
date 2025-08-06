# Multilingual AI Translation System

A modular, AI-driven multilingual translation web app built with Hugging Face’s Transformers (PyTorch backend) using Helsinki-NLP’s pre-trained MarianMT models. The system includes intelligent preprocessing steps like contraction expansion and spell correction to improve translation quality. Deployed as a Flask app with a simple user interface for real-time translations.

---

## Features

- Supports multiple language pairs (English, German, French, Spanish, Italian, Russian)
- Utilizes Helsinki-NLP MarianMT models for high-quality neural machine translation
- Preprocessing includes:
  - English contraction expansion (e.g., "I'm" → "I am")
  - Spell correction with SymSpell for supported languages
- Modular architecture with separate components for language handling, preprocessing, translation, and app interface
- Flask web app for easy deployment and real-time translations

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/multilingual-translation.git
   cd multilingual-translation

### Install Dependencies

pip install -r requirements.txt

## Usage

### Run the Flask App

python app.py
Open your browser and navigate to: http://127.0.0.1:5000/

Enter the source language, target language, and text to translate. The app preprocesses input, performs translation, and displays the result.

## Project Structure 
.
├── app.py                  # Flask web app

├── languages.py            # Language codes and model name generation

├── preprocessing.py        # Text preprocessing: contraction expansion & spell correction

├── translator.py           # Translation functions using Hugging Face MarianMT

├── resources/              # Frequency dictionaries for SymSpell spell correction

├── templates/
│   └── index.html          # Web UI template (Flask)

├── contractions_dict.py    # English contractions dictionary

├── requirements.txt        # Python dependencies

└── README.md

## Notes

The first time you translate between language pairs, the MarianMT models are downloaded automatically by Hugging Face.

Spell correction relies on SymSpell dictionaries placed in the resources/ directory — make sure to download appropriate frequency dictionaries for your target languages.

Currently, contraction expansion is implemented only for English.

Model loading happens per translation request; for production use, consider loading models once at app startup to improve performance.

Feel free to reach out for questions or contributions!

