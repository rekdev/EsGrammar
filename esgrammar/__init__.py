"""
=========
EsGrammar
=========
Short python library for check varius grammar things in spanish text.
"""

from .syllable import Syllable
from .grammar import Grammar


def analyze(words: list) -> list:
    """
    Analyze a word list and return its gramatical info.
    """
    words_analyzed = []

    for word in words:
        slb = Syllable(word)
        gmr = Grammar(word)

        words_analyzed.append(
            {
                "syllables": slb.get(),
                "vowels": gmr.get_vowels(),
                "consonants": gmr.get_consonants(),
                "tone_syllable": slb.get_tone(),
                "tone_syllable_index": slb.get_tone_index(),
                "type": gmr.get_type()
            }
        )

    return words_analyzed
