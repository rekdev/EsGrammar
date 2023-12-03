from .syllable import Syllable
from .grammar import Grammar

def analyze(words: str) -> list:
    """
    Analyze a word list splited by spaces.
    """
    words = words.split()
    words_analyzed = []

    for word in words:
        slb = Syllable(word)
        gmr = Grammar(word)

        words_analyzed.append(
            {
                "syllables": slb.get(),
                "tone_syllable": slb.get_tone(),
                "tone_syllable_index": slb.get_tone_index(),
                "type": gmr.get_type()
            }
        )
    
    return words_analyzed
