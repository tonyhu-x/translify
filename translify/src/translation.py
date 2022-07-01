"""This module provides translation from any language other than English to English."""

from transformers import pipeline

translators = {
    "arabic": "Helsinki-NLP/opus-mt-ar-en",
    "bengali": "Helsinki-NLP/opus/mt-bn-en",
    "cantonese": "Helsinki-NLP/opus-mt-zh-en",
    # Multiple "chinese" languages, dialects and topolects are translated by this model
    "chinese": "Helsinki-NLP/opus-mt-zh-en",
    "french": "Helsinki-NLP/opus-mt-fr-en",
    "hindi": "Helsinki-NLP/opus-mt-hi-en",
    "indonesian": "Helsinki-NLP/opus-mt-id-en",
    "mandarin": "Helsinki-NLP/opus-mt-zh-en",
    "portugese": "unicamp-dl/translation-pt-en-t5",
    "russian": "Helsinki-NLP/opus-mt-ru-en",
    "spanish": "Helsinki-NLP/opus-mt-es-en"
}

two_letter_codes = {
    "ar": "arabic",
    "bn": "bengali",
    "de": "german",
    # "en": "english",
    "es": "spanish",    # Technically also refers to Castillian
    "fr": "french",
    "hi": "hindi",
    "id": "indonesian",
    "pt": "portuguese",
    "ru": "russian",
    "zh": "mandarin",   # Technically zh refers to all "Chinese" languages, dialects and topolects
}


def translate(text, language=None, two_letter=None):
    """Translates the text from the given language to English and returns the text.

    Raises ValueError if the language (by the language or two_letter parameter) is not specified
    or if the language is unsupported. If both language and two_letter parameters are given,
    then the language parameter takes precedence.
    """
    if language is None and two_letter is None:
        raise ValueError("Language not specified.")
    elif not language and two_letter:
        language = two_letter_codes[two_letter] if two_letter in two_letter_codes else None
    
    if language not in translators:
        raise ValueError("Unsupported language. Please verify that there is no typo.")
    
    # TODO: Download the models in advance in a folder like ~/.trans_models/...
    translator = pipeline("translation", model=translators[language])
    result = translator(text)

    return result["translation_text"]