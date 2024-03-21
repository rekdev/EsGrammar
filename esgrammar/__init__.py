"""
=========
EsGrammar
=========
Small library for checking the spelling and grammar things of words in the Spanish language.
"""
from .word import Word


def analyse(words: list) -> list:
    """
    This function takes a list of words as input and returns their corresponding grammatical information.

    Args:
        words (list): List of words to be analysed.

    Returns:
        list: List with grammatical information for each word in the list
    """
    words_analyzed = []

    for word_item in words:
        wd = Word(word_item)

        words_analyzed.append({
            "word": wd.value,
            "syllables": wd.syllables,
            "tonic_syllable": wd.tonic_syllable,
            "tonic_syllable_index": wd.tonic_syllable_index,
            "vowels": wd.vowels,
            "consonants": wd.consonants,
            "type": wd.type
        })

    return words_analyzed
