# Import the preprocessing function from the preprocessing module
from preprocessing import preprocess_input

# Import the translate function from the translator module
from translator import translate

# Import the dictionary of supported language codes
from languages import LANGUAGE_CODES

# Function to check if the input language is supported
def is_valid_language(language):
    return language.lower() in LANGUAGE_CODES

# Function to generate the Hugging Face model name based on source and target languages
def get_model_name(source, target):
    source_code = LANGUAGE_CODES[source]  # Get the code for the source language
    target_code = LANGUAGE_CODES[target]  # Get the code for the target language
    return f"Helsinki-NLP/opus-mt-{source_code}-{target_code}"  # Construct the model name
 
# Main function that drives the CLI tool
def main():
    print("Multilingual Translation CLI Tool\n")  # Print tool title

    # Prompt user to enter the source language
    source_language = input("Enter source language (e.g., english): ").lower()

    # Validate if the entered source language is supported
    if not is_valid_language(source_language):
        print(f"Error: '{source_language}' is not a supported source language.")  # Show error message
        return  # Exit the program

    # Prompt user to enter the target language
    target_language = input("Enter target language (e.g., german): ").lower()

    # Validate if the entered target language is supported
    if not is_valid_language(target_language):
        print(f"Error: '{target_language}' is not a supported target language.")  # Show error message
        return  # Exit the program

    # Prompt user to enter the text to translate
    input_text = input("Enter text to translate: ").strip()

    # Check if the input text is empty
    if not input_text:
        print("Error: Input text cannot be empty.")  # Show error message
        return  # Exit the program

    try:
        # Get the Hugging Face model name using the source and target languages
        model_name = get_model_name(source_language, target_language)

        # Convert full language name to code (e.g., "english" -> "en")
        lang_code = LANGUAGE_CODES[source_language]

        # Preprocess input: expand contractions and correct spelling for the source language
        clean_text = preprocess_input(input_text, lang_code)

        # Call the translate function and get the translated result
        translated_text = translate(clean_text, model_name)

        # Display the translated output
        print(f"\n Translated: {translated_text}")

    except Exception as e:
        # Handle any errors during model loading or translation
        print("An error occurred during translation.")
        print(f"Details: {e}")  # Print the error details for debugging

# This ensures the main function only runs when this script is executed directly
if __name__ == "__main__":
    main()
