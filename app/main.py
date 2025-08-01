# if __name__ == "__main__": means: only run this part when you run this file directly (not when it's imported into another script).
# input_text: this is your test sentence.
# model_name: you specify the model here.
# it calls translate() and prints both the original and translated versions.
# main.py
import argparse
from translator import translate
from languages import LANGUAGE_CODES

def main():
    parser = argparse.ArgumentParser(description="Multilingual Translation Tool")
    parser.add_argument("-s", "--source", type=str, required=True, help="Source language (e.g. english)")
    parser.add_argument("-t", "--target", type=str, required=True, help="Target language (e.g. german)")
    parser.add_argument("-i", "--input", type=str, required=True, help="Text to translate")

    args = parser.parse_args()

    source_language = args.source.lower()
    target_language = args.target.lower()
    input_text = args.input

    if source_language not in LANGUAGE_CODES or target_language not in LANGUAGE_CODES:
        print(f"Supported languages are: {', '.join(LANGUAGE_CODES.keys())}")
        return

    source_code = LANGUAGE_CODES[source_language]
    target_code = LANGUAGE_CODES[target_language]
    model_name = f"Helsinki-NLP/opus-mt-{source_code}-{target_code}"

    translated_text = translate(input_text, model_name)
    print(f"Original: {input_text}")
    print(f"Translated: {translated_text}")

if __name__ == "__main__":
    main()
