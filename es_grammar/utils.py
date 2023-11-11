def has_vowel(x: str, strongers: bool = True) -> bool:
    """
    Check if a text slice contains vowels.
    """

    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ" if strongers else "aeiouAEIOU"
    has_vowel = False

    for letter in x:
        for vowel in vowels:
            if vowel == letter:
                has_vowel = True

    return has_vowel

def has_consonant(x: str) -> bool:
    """
    Check if a text slice contains consonants.
    """
    
    return not has_vowel(x)
