"""Exports two functions: english_to_french and french_to_english."""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translates given string english_text to French."""
    e2f_translator = MyMemoryTranslator("en", "fr")
    french_text = e2f_translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translates given string french_text to English."""
    f2e_translator = MyMemoryTranslator("fr", "en")
    english_text = f2e_translator.translate(french_text)
    return english_text
