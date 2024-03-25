def has_vowels(x: str) -> bool:
    """
    Checks if slice of text contains vowels.

    Args:
        x (str): Slice of some text.

    Returns:
        bool: Value that indicates if the slice contains vowels.
    """
    value = False
    vowels = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

    for letter in x:
        if letter.lower() in vowels:
            value = True
            break

    return value


def has_consonants(x: str) -> bool:
    """
    Checks if slice of text contains consonants.

    Args:
        x (str): Slice of some text.

    Returns:
        bool: Value that indicates if the slice contains consonants.
    """
    value = False
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    for letter in x:
        if letter.lower() in consonants:
            value = True
            break

    return value


def is_consonant_group(x: str) -> bool:
    """
    Checks if slice of text matches at spanish consonant group.

    Args:
        x (str): Slice of some text.

    Returns:
        bool: Value that indicates if the slice matches with some group.
    """
    consonant_groups = ["cl", "bl", "gl", "gr", "gn", "ll", "pl",
                        "tl", "cr", "br", "dr", "fr", "pr", "tr", "ch", "ps", "rr"]

    return x.lower() in consonant_groups
