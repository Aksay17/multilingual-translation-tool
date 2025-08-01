# if __name__ == "__main__": means: only run this part when you run this file directly (not when it's imported into another script).
# input_text: this is your test sentence.
# model_name: you specify the model here.
# it calls translate() and prints both the original and translated versions.
from translator import translate
from languages import get_model_name

if __name__ == "__main__":
    source_language = "english"
    target_language = "italian"
    input_text = "Hello, how are you today?"

    try:
        model_name = get_model_name(source_language, target_language)
        translated_text = translate(input_text, model_name)

        print("Original:", input_text)
        print("Translated:", translated_text if translated_text else "⚠️ No translation output")

    except ValueError as e:
        print("⚠️", e)
