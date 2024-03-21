"""
=========
EsGrammar
=========
Small library for checking the spelling and grammar things of words in the Spanish language.
"""
from .word import Word


def analyze(words: list) -> list:
    words_analyzed = []

    for word_item in words:
        wd = Word(word_item)

        words_analyzed.append(
            {
                "word": word_item,
                "syllables": wd.syllables,
                "tonic_syllable": wd.tonic_syllable,
                "tonic_syllable_index": wd.tonic_syllable_index,
                "vowels": wd.vowels,
                "consonants": wd.consonants,
                "type": wd.type
            }
        )

    return words_analyzed
