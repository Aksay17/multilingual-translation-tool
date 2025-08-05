from flask import Flask, render_template, request
from preprocessing import preprocess_input
from translator import translate
from languages import LANGUAGE_CODES, get_model_name

app = Flask(__name__)

def is_valid_language(language):
    return language.lower() in LANGUAGE_CODES

def is_same_language(target_language, source_language):
    print(f"Checking if target '{target_language}' is the same as source '{source_language}'")
    return target_language.lower() == source_language.lower()

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    error = ""
    source_language = ""
    target_language = ""
    input_text = ""

    if request.method == "POST":
        print("Received POST request with form data")
        source_language = request.form.get("source_language", "").lower()
        target_language = request.form.get("target_language", "").lower()
        input_text = request.form.get("input_text", "").strip()

        # Validate languages and input
        if not is_valid_language(source_language):
            error = f"Unsupported source language: {source_language}"
        elif not is_valid_language(target_language):
            error = f"Unsupported target language: {target_language}"
        elif not input_text:
            error = "Input text cannot be empty."
        elif is_same_language(target_language, source_language):
            error = "Please select different source and target language."
        else:
            try:
                model_name = get_model_name(source_language, target_language)
                clean_text = preprocess_input(input_text, lang_code=LANGUAGE_CODES[source_language])
                translation = translate(clean_text, model_name)
            except Exception as e:
                error = f"Error during translation: {e}"

    return render_template("index.html",
                           translation=translation,
                           error=error,
                           source_language=source_language,
                           target_language=target_language,
                           input_text=input_text,
                           languages=LANGUAGE_CODES.keys())

if __name__ == "__main__":
    app.run(debug=True)
