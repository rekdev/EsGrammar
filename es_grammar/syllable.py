from .utils import has_vowel, has_consonant

class Syllable:
    def __init__(self, word):
        self.word = word

    def merge_vowels(self):
        word = self.word
        word_lenght = len(word)
        count = 0
        merged_vowels = []

        while count < word_lenght:
            letter = word[count]
            next_letter = word[count + 1] if count + 1 < word_lenght else ""
            next_letter2 = word[count + 2] if count + 2 < word_lenght else ""

            if has_vowel(letter) and has_vowel(next_letter) and has_vowel(next_letter2):
                merged_vowels.append(letter + next_letter + next_letter2)
                count+=2

            elif has_vowel(letter) and has_vowel(next_letter):
                merged_vowels.append(letter + next_letter)
                count+=1

            else:
                merged_vowels.append(letter)

            count+=1

        return merged_vowels 


    def get_syllables(self):
        pass