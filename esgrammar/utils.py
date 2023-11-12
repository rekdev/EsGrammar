def has_vowel(x: str, strongers: bool = True) -> bool:
    """
    Check if a text slice contains vowels.
    """

    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ" if strongers else "aeiouAEIOU"
    hs_vw = False
    for letter in x:
        for vowel in vowels:
            if vowel == letter:
                hs_vw = True

    return hs_vw

def has_consonant(x: str) -> bool:
    """
    Check if a text slice contains consonants.
    """
    return not has_vowel(x)

def is_consonant_group(x: str) -> bool:
    "check if the string is an indivisible consonant group."
    consonant_groups = ["cl", "bl", "gl", "ll", "pl", "tl", "cr", "br", "dr", "fr", "pr", "tr", "ch", "th", "ps", "gn", "rr"]
    is_cs_gp = False
    x = x.lower()

    for consonant_group in consonant_groups:
        if consonant_group == x:
            is_cs_gp = True

    return is_cs_gp