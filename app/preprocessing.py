import os
import re
from symspellpy.symspellpy import SymSpell, Verbosity
from contractions_dict import contractions_dict

# Path to the resources directory where frequency dictionary files are stored
RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resources")

# SymSpell configuration
MAX_EDIT_DISTANCE = 2
PREFIX_LENGTH = 7

# Dictionary to store initialized SymSpell instances per language
symspell_instances = {}

def expand_contractions(text, lang_code):
    """
    Expands contractions if the language is English.
    Also handles sloppy inputs like "im" (no apostrophe).
    """
    if lang_code != "en":
        return text  # No expansion for other languages

    # Compile regex to match any contraction in the dictionary
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in contractions_dict.keys()) + r')\b', flags=re.IGNORECASE)

    # Replace with expanded form, maintaining case
    def replace(match):
        word = match.group(0)
        expanded = contractions_dict.get(word.lower(), word)
        return expanded if word.islower() else expanded.capitalize()

    return pattern.sub(replace, text)

def initialize_symspell(lang_code):
    """
    Loads and initializes SymSpell with the frequency dictionary for the specified language.
    """
    if lang_code in symspell_instances:
        return  # Already loaded

    sym_spell = SymSpell(max_dictionary_edit_distance=MAX_EDIT_DISTANCE, prefix_length=PREFIX_LENGTH)
    dict_filename = f"{lang_code}_frequency_dictionary.txt"
    dict_path = os.path.join(RESOURCE_DIR, dict_filename)

    if not os.path.exists(dict_path):
        print(f"[Warning] Dictionary not found for '{lang_code}': {dict_path}")
        return

    try:
        sym_spell.load_dictionary(dict_path, term_index=0, count_index=1, encoding="utf-8")
        symspell_instances[lang_code] = sym_spell
    except Exception as e:
        print(f"[Error] Failed to load SymSpell dictionary for '{lang_code}': {e}")

def correct_spelling(text, lang_code):
    """
    Corrects spelling in the given text using SymSpell for the specified language.
    """
    initialize_symspell(lang_code)
    sym_spell = symspell_instances.get(lang_code)

    if not sym_spell:
        return text  # If dictionary missing, return text unchanged

    corrected_words = []

    for word in text.split():
        # Strip punctuation
        clean_word = re.sub(r'[^\w\s]', '', word)

        # Find the closest suggestion
        suggestions = sym_spell.lookup(clean_word, Verbosity.CLOSEST, max_edit_distance=MAX_EDIT_DISTANCE)
        corrected = suggestions[0].term if suggestions else clean_word
        corrected_words.append(corrected)

    return ' '.join(corrected_words)

def preprocess_input(text, lang_code):
    """
    Main preprocessing function: expands contractions and corrects spelling.
    """
    expanded_text = expand_contractions(text, lang_code)  # English only
    corrected_text = correct_spelling(expanded_text, lang_code)  # All supported languages
    return corrected_text