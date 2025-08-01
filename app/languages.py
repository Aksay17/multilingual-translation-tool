#Stores supported languages
# Provides a function to get model names (e.g., English to German)

# Dictionary mapping language names to codes used by Helsinki-NLP
# languages.py

# Dictionary mapping language names to codes used by Helsinki-NLP
LANGUAGE_CODES = {
    "english": "en",
    "german": "de",
    "french": "fr",
    "spanish": "es",
    "italian": "it",
    "portuguese": "pt",
    "russian": "ru"
}

def get_model_name(source_lang: str, target_lang: str) -> str:
    """Generate the HuggingFace model name for given source and target languages."""
    source_code = LANGUAGE_CODES.get(source_lang.lower())
    target_code = LANGUAGE_CODES.get(target_lang.lower())

    if source_code and target_code:
        return f"Helsinki-NLP/opus-mt-{source_code}-{target_code}"
    else:
        raise ValueError(f"Unsupported language combination: {source_lang} → {target_lang}")
