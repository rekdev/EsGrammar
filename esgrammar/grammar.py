from .syllable import Syllable
from .utils import has_vowel, has_consonant


class Grammar:
    """
    This class contains some functions for check some issues of a word grammar.
    """

    def __init__(self, word):
        self.word = word

    def get_type(self) -> int:
        """
        Return a word type with number, in spanish, the types are:

        1: Oxytone
        2. Paroxytone
        3. Proparoxytone
        4. Superproparoxytone
        """
        word = self.word
        slb = Syllable(word)
        syllables = slb.get()

        return (slb.get_tone_index() - len(syllables)) * - 1

    def get_vowels(self) -> list:
        """
        Get vowels list of a word.
        """
        word = self.word
        vowel_list = []

        for letter in word:
            if has_vowel(letter):
                vowel_list.append(letter)

        return vowel_list

    def get_consonants(self) -> list:
        """
        Get consonants list of a word.
        """
        word = self.word
        consonant_list = []

        for letter in word:
            if has_consonant(letter):
                consonant_list.append(letter)

        return consonant_list
