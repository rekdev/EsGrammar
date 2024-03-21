def has_vowels(x: str) -> bool:
    """
    Checks if slice of text contains vowels.
    """
    value = False
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"

    for letter in x:
        if letter in vowels:
            value = True
            break

    return value


def has_consonants(x: str) -> bool:
    """
    Checks if slice of text contains consonants.
    """
    return not has_vowels(x)


def is_consonant_group(x: str) -> bool:
    """
    Checks if slice of text matches at spanish consonant group.
    """
    consonant_groups = ["cl", "bl", "gl", "gr", "gn", "ll", "pl",
                        "tl", "cr", "br", "dr", "fr", "pr", "tr", "ch", "ps", "rr"]

    return x.lower() in consonant_groups

