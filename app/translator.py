# Importing MarianMTModel and MarianTokenizer from Hugging Face's transformers library:
# - MarianMTModel is the machine translation model (used for actual translation).
# - MarianTokenizer converts text to token IDs (numbers) that the model can process,
#   and then back to human-readable text after prediction.
# Think of the tokenizer as a translator between human language and model language.
from transformers import MarianMTModel, MarianTokenizer

# It takes a model_name like "Helsinki-NLP/opus-mt-en-de" as input.
# It downloads and loads the tokenizer and model from Hugging Face’s Model Hub.
# from_pretrained(model_name) looks up the model name online, downloads it the first time, 
# and reuses it later from cache.
# It returns both:
# The tokenizer: turns your input sentence into model-readable format.
# The model: the neural network that does the actual translation.
# You use this function to keep your code modular and clean. 
# Instead of loading models every time manually, you call this once.

def load_model(model_name):
    """Load the tokenizer and model from Hugging Face."""
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

#This function takes two parameters:
# text: the sentence you want to translate.
# model_name: optional, defaults to English → German.
# It calls load_model(), so you now have your tokenizer and model ready.

def translate(text, model_name="Helsinki-NLP/opus-mt-en-de"):
    """Translate text using the specified model."""
    if not text.strip():
        print("Empty input text. Nothing to translate.")
        return None
    
    tokenizer, model = load_model(model_name)

# This line converts your sentence into tokens (numbers the model understands).
# return_tensors="pt" means: return as PyTorch tensors (the format that MarianMTModel expects).
# padding=True: ensures all inputs are of the same length (important if batch translating multiple sentences).
# Example: "Hello, world!" → [117, 83, 42] → model can now work with this.

    inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)

# model.generate() is a high-level Hugging Face function that:
# Runs the model in inference mode (no training).
# Takes the tokenized input and returns predicted token IDs for the translated sentence.
# **inputs passes all keyword arguments from the tokenizer (like input_ids, attention_mask).
# The model outputs something like [43, 221, 9, 1] which maps to German words.

    # Generate translation
    try:
        translated = model.generate(**inputs)
        output = tokenizer.decode(translated[0], skip_special_tokens=True)
        return output
    except Exception as e:
        print("⚠️ Error during translation:", e)
        return None

# output = tokenizer.decode(translated[0], skip_special_tokens=True)
# This converts the predicted token IDs back into human-readable language.
# translated[0] because the output is a list (even if just one sentence).
# skip_special_tokens=True removes things like <pad>, <eos> which are used internally by models but not meant for humans.
# This step transforms model output into: "Hallo, wie geht es dir heute?"






