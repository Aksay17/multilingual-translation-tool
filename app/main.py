# if __name__ == "__main__": means: only run this part when you run this file directly (not when it's imported into another script).
# input_text: this is your test sentence.
# model_name: you specify the model here.
# it calls translate() and prints both the original and translated versions.
# main.py
from languages import LANGUAGE_CODES
from translator import translate

def choose_language(prompt):
    print(prompt)
    for i, lang in enumerate(LANGUAGE_CODES.keys(), 1):
        print(f"{i}. {lang.capitalize()}")
    choice = int(input("Enter number: "))
    lang_name = list(LANGUAGE_CODES.keys())[choice - 1]
    return LANGUAGE_CODES[lang_name]

def main():
    print("Welcome to Multilingual Translation CLI!")
    
    source_code = choose_language("Select source language:")
    target_code = choose_language("Select target language:")
    
    text = input("Enter text to translate: ")
    
    model_name = f"Helsinki-NLP/opus-mt-{source_code}-{target_code}"
    
    print(f"Translating using model: {model_name} ...")
    
    translated_text = translate(text, model_name)
    print(f"Translated text:\n{translated_text}")

if __name__ == "__main__":
    main()
