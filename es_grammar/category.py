class Category:
    def __init__(self, word):
        self.word = word

    def is_vowel(self, letter):
        return "aeiouáéíóúAEIOUÁÉÍÓÚ".find(letter) != -1

    def is_consonant(self, letter):
        return not self.is_vowel(letter) 

    def categorize(self):
        categorized = []

        count = 0
        word_lenght = len(self.word)

        while count < word_lenght:
            letter = self.word[count]
            next_letter = self.word[count + 1] if count + 1 < word_lenght else ""
            next_letter2 = self.word[count + 2] if count + 2 < word_lenght else ""

            if self.is_consonant(letter):
                categorized.append({
                    "type": "C",
                    "str": letter
                })
            elif self.is_vowel(letter) and self.is_vowel(next_letter) and self.is_vowel(next_letter2):
                categorized.append({
                    "type": "V",
                    "str": letter + next_letter + next_letter2
                })

                count+=2
            elif self.is_vowel(letter) and self.is_vowel(
                
            ):
                categorized.append({
                    "type": "V",
                    "str": letter + next_letter
                })

                count+=1
            elif self.is_vowel(letter):
                categorized.append({
                    "type": "V",
                    "str": letter
                })

            count+=1

        return categorized

        def get_statics(self):
            pass