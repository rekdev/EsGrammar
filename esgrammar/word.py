from .utils import has_consonants, has_vowels, is_consonant_group


class Word:
    """
    This class provides core functionality of word grammar.

    Attributes:
        syllables (list): Word split into syllables.
        tonic_syllable (str): Tonic syllable obtained based on Spanish accentuation rules.
        tonic_syllable_index (int): Index of tonic syllable.
        vowels (list): List of the all vowels.
        consonants (list): List of the all consonants.
        type (str | None): Grammatical classification based on Spanish accentuation rules.
        value (str): Contains public access word attribute of the class.
    """
    __vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    __accented_vowels = ["á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]
    __closed_vowels = ["i", "u", "I", "U"]
    __open_vowels = ["a", "e", "o", "A", "E", "O"]
    __closed_vowels_accented = ["i", "u", "I", "U", "í", "ú", "Í", "Ú"]
    __open_vowels_accented = ["a", "e", "o", "A", "E", "O", "á", "é", "ó", "Á", "É", "Ó"]
    __umlauts = ["ü", "Ü"]
    __case_consonants = ["n", "s", "N", "S"]

    def __init__(self, x: str):
        """
        Args:
            x (str): Any word in spanish language.
        """
        if x == "":
            raise ValueError("x should not be an empty string.")

        self.__word = x
        self.syllables = self.__get_syllables()
        self.tonic_syllable = self.__get_tonic_syllable()
        self.tonic_syllable_index = self.__get_tonic_syllable_by_index()
        self.vowels = self.__get_vowels()
        self.consonants = self.__get_consonants()
        self.type = self.__get_type()
        self.value = self.__word

    def __get_syllables(self) -> list:
        """
        Split word by syllables, using spanish grammar rules.

        Returns:
            list: Syllable list.
        """
        merged_vowels = []
        word_len = len(self.__word)
        i = 0

        # First pass: Merging vowels in special cases.
        while i < word_len:
            letter = self.__word[i]
            next_letter = self.__word[i + 1] if i + 1 < word_len else ""
            next_two_letter = self.__word[i + 2] if i + 2 < word_len else ""

            # Checks if slice is a triphthong.
            if ((
                letter in self.__closed_vowels_accented
                and next_letter in self.__open_vowels_accented
                and next_two_letter in self.__closed_vowels_accented
            ) or (
                letter in self.__open_vowels_accented
                and next_letter in self.__closed_vowels_accented
                and next_two_letter in self.__open_vowels_accented
            )):
                merged_vowels.append(letter + next_letter + next_two_letter)
                i += 2

            # Checks if slice is a diphthong or umlaut case.
            elif ((
                letter in self.__open_vowels_accented
                and next_letter in self.__closed_vowels
            ) or (
                letter in self.__closed_vowels
                and next_letter in self.__open_vowels_accented
            ) or (
                letter in self.__umlauts
                and next_letter in self.__vowels
            ) or (letter in "uU" and next_letter in "iI")):
                merged_vowels.append(letter + next_letter)
                i += 1

            else:
                merged_vowels.append(letter)

            i += 1

        # Second pass: Merge vowel slices with the corresponding consonant.
        syllables = []
        consonants_count = 0
        merged_vowels_len = len(merged_vowels)
        j = 0

        while j < merged_vowels_len:
            tmp_slice = merged_vowels[j]
            next_slice = merged_vowels[j + 1] if j + \
                1 < merged_vowels_len else ""
            prev_slice = merged_vowels[j - 1] if j - 1 >= 0 else ""

            if has_consonants(tmp_slice):
                consonants_count += 1

            if consonants_count == 1 and has_vowels(next_slice):
                tmp_slice += next_slice
                j += 1
                consonants_count = 0

            elif (
                consonants_count == 1
                and not is_consonant_group(tmp_slice + next_slice)
                and (has_consonants(next_slice) or next_slice == "")
            ):
                syllables_len = len(syllables)

                if syllables_len > 0:
                    syllables[syllables_len - 1] += tmp_slice

                consonants_count = 0

            elif (
                consonants_count == 2
                and is_consonant_group(prev_slice + tmp_slice)
                and has_vowels(next_slice)
            ):
                tmp_slice = prev_slice + tmp_slice + next_slice
                j += 1
                consonants_count = 0

            syllable = tmp_slice

            if (
                syllable != ""
                and not (len(syllable) == 1
                         and has_consonants(syllable))
            ):
                syllables.append(syllable)

            j += 1

        return syllables

    def __get_tonic_syllable(self) -> str:
        """
        Returns:
            str: Tonic syllable.
        """
        return self.syllables[self.__get_tonic_syllable_by_index()]

    def __get_tonic_syllable_by_index(self) -> int:
        """
        Determine the index of the tonic syllable in the syllable list.

        Returns:
            int: Index of the tonic syllable.
        """
        syllables_len = len(self.syllables)
        word_len = len(self.__word)
        last_letter = self.__word[word_len - 1] if word_len - 1 >= 0 else ""

        if (
            last_letter in self.__case_consonants
            or last_letter in self.__vowels
        ):
            tonic_index = syllables_len - 2 if syllables_len - 2 >= 0 else 0
        else:
            tonic_index = syllables_len - 1 if syllables_len - 1 >= 0 else 0

        for i, syllable in enumerate(self.syllables):
            for letter in syllable:
                if letter in self.__accented_vowels:
                    tonic_index = i

        return tonic_index

    def __get_vowels(self) -> list:
        """
        Returns:
             list: List with all vowels of the word.
        """
        return [letter for letter in self.__word if has_vowels(letter)]

    def __get_consonants(self) -> list:
        """
        Returns:
            list: List with all consonants of the word.
        """
        return [letter for letter in self.__word if has_consonants(letter)]

    def __get_type(self) -> str | None:
        """
        Returns the grammatical classification of the given word.

        Returns:
            str: Classification in Spanish grammar.
            None: If it does not correspond to any classification.
        """
        word_type = None
        type_by_number = (self.__get_tonic_syllable_by_index() - len(self.syllables)) * -1

        if len(self.syllables) == 1:
            word_type = "monosilaba"
        elif type_by_number == 1:
            word_type = "oxitona"
        elif type_by_number == 2:
            word_type = "paroxitona"
        elif type_by_number == 3:
            word_type = "proparoxitona"
        elif type_by_number > 3:
            word_type = "superproparoxitona"

        return word_type

    def __str__(self):
        return f"<{self.__word} with {len(self.syllables)} syllables and {self.type} type.>"
