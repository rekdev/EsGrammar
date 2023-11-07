from category import Category 

class Syllable:
    def __init__(self, word):
        self.category = Category(word)

    def syllabize(self):
        pass