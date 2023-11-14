from esgrammar import Syllable

word = str(input("Enter a word: "))
slb = Syllable(word)

print(slb.get_syllables())