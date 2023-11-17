def has_vowel(x: str) -> bool:
    """
    Check if a text slice contains vowels.
    """

    vowels = "aeiouáéíóú"
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


def is_consonant_group(x: str) -> bool:
    "Check if the string is an indivisible consonant group."
    consonant_groups = ["cl", "bl", "gl", "ll", "pl", "tl", "cr",
                        "br", "dr", "fr", "pr", "tr", "ch", "ps", "gn", "rr"]
    x = x.lower()

    return x in consonant_groups
