"""
=========
EsGrammar
=========
Small library for checking the spelling and grammar things of words in the Spanish language.
"""
import regex
from .word import Word


def analyse_word_list(word_list: list) -> list:
    """
    This function takes a list of words as input and returns their corresponding grammatical information.

    Args:
        word_list (list): List of words to be analysed.

    Returns:
        list: List of grammatical information for each word in the list
    """
    words_analysed = []

    for word_item in word_list:
        wd = Word(word_item)

        words_analysed.append({
            "word": wd.value,
            "syllables": wd.syllables,
            "tonic_syllable": wd.tonic_syllable,
            "tonic_syllable_index": wd.tonic_syllable_index,
            "vowels": wd.vowels,
            "consonants": wd.consonants,
            "type": wd.type
        })

    return words_analysed


def analyse_text(text: str) -> list:
    """
    This function analyses individual words in a given text and returns their corresponding grammatical data.

    Args:
        text (str): The text that will be analysed.

    Returns:
        list: List of grammatical information for each word in the text.
    """
    pattern = r"[\p{P}\p{S}]|\n|\\."
    word_list = regex.sub(pattern, "", text).split()
    words_analysed = analyse_word_list(word_list)

    return words_analysed
