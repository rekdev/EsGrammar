def has_vowel(x):
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    has_vowel = False

    for letter in x:
        for vowel in vowels:
            if vowel == letter:
                has_vowel = True

    return has_vowel

def has_consonant(x):
    return not has_vowel(x)
