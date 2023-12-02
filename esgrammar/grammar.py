from .syllable import Syllable

class Grammar:
    def __init__(self, word):
        self.word = word

    def get_type(self) -> int:
        """
        Return a word type with number, in spanish, the types are:

        1. Aguda
        2. Grave
        3. Esdrújula
        4. Sobresdrújula
        """
        word = self.word
        slb = Syllable(word)
        syllables = slb.get()
        syllables_lenght = len(syllables)
        tone_index = slb.get_tone_index()

        word_type = 0

        if tone_index == syllables_lenght - 1:
            word_type = 1
        elif tone_index == syllables_lenght - 2:
            word_type = 2
        elif tone_index == syllables_lenght - 3:
            word_type = 3
        elif tone_index == syllables_lenght - 4:
            word_type = 4
        
        return word_type

