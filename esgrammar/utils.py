def has_vowel(x: str, strongers: bool = True) -> bool:
    """
    Check if a text slice contains vowels.
    """

    vowels = "aeiouáéíóú" if strongers else "aeiou"
    hs_vw = False
    x = x.lower()

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

def is_open_vowel(x: str) -> bool:
    vowels = "aeo"
    is_op_vw = False
    x = x.lower()

    for vowel in vowels:
        if vowel == x:
            is_op_vw = True

    return is_op_vw

def is_closed_vowel(x: str) -> bool:
    vowels = "iu"
    is_cl_vw = False
    x = x.lower()

    for vowel in vowels:
        if vowel == x:
            is_cl_vw = True

    return is_cl_vw

def is_consonant_group(x: str) -> bool:
    "check if the string is an indivisible consonant group."
    consonant_groups = ["cl", "bl", "gl", "ll", "pl", "tl", "cr", "br", "dr", "fr", "pr", "tr", "ch", "th", "ps", "gn", "rr"]
    is_cs_gp = False
    x = x.lower()

    for consonant_group in consonant_groups:
        if consonant_group == x:
            is_cs_gp = True

    return is_cs_gp