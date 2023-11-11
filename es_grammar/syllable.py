from .utils import has_vowel, has_consonant

class Syllable:
    """
    This class contains varius methods from process words and get its syllables info.
    """

    def __init__(self, word: str):
        self.word = word

    def merge_vowels(self) -> list:
        """
        Take word and merge its vowels if not contains strong cases.
        """

        word = self.word
        word_lenght = len(word)
        count = 0
        merged_vowels = []
        vowel = lambda x: has_vowel(x, False)

        while count < word_lenght:
            letter = word[count]
            next_letter = word[count + 1] if count + 1 < word_lenght else ""
            next_letter2 = word[count + 2] if count + 2 < word_lenght else ""

            if vowel(letter) and vowel(next_letter) and vowel(next_letter2):
                merged_vowels.append(letter + next_letter + next_letter2)
                count+=2

            elif vowel(letter) and vowel(next_letter):
                merged_vowels.append(letter + next_letter)
                count+=1

            else:
                merged_vowels.append(letter)

            count+=1

        return merged_vowels 


    def get_syllables(self) -> list:
        """
        Split a word in syllables and return syllable list.
        """
        
        word = self.word
        merged_vowels = self.merge_vowels(word)
        merged_vowels_lenght = len(merged_vowels)
        syllables = []
        consonants_count = 0
        count = 0

        while count < merged_vowels_lenght:
            syllable = ""
            tmp_slice = merged_vowels[count]

            if has_consonant(tmp_slice):
                consonants_count+=1

            if syllable != "":
                syllables.append(syllable)

            count+=1

        return syllables