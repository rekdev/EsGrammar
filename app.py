from esgrammar import Syllable

word = str(input("Input a word: "))
slb = Syllable(word)

print(slb.get_syllables())
