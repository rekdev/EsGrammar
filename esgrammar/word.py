from .utils import has_consonants, has_vowels, is_consonant_group


class Word:
    __vowels = "aeiouAEIOU"
    __accented_vowels = "áéíóuÁÉÍÓÚ"
    __closed_vowels = "iuíuIUÍÚ"
    __open_vowels = "aeoáéóAEOÁÉÓ"
    __umlauts = "üÜ"
    __case_consonants = "nsNS"

    def __init__(self, x: str):
        self.__word = x
        self.syllables = self.__get_syllables()
        self.tonic_syllable = self.__get_tonic_syllable()
        self.tonic_syllable_index = self.__get_tonic_syllable_by_index()
        self.vowels = self.__get_vowels()
        self.consonants = self.__get_consonants()
        self.type = self.__get_type()

    def __get_syllables(self) -> list:
        """
        Returns list with syllables of the word.
        """
        merged_vowels = []
        word_len = len(self.__word)
        i = 0

        # First pass: Merging vowels in special cases.
        while i < word_len:
            letter = self.__word[i]
            next_letter = self.__word[i + 1] if i + 1 < word_len else ""
            next_two_letter = self.__word[i + 2] if i + 2 < word_len else ""

            # Check if slice is a triphthong.
            if ((
                letter in self.__closed_vowels
                and next_letter in self.__open_vowels
                and next_two_letter in self.__closed_vowels
            ) or (
                letter in self.__open_vowels
                and next_letter in self.__closed_vowels
                and next_two_letter in self.__open_vowels
            )):
                merged_vowels.append(letter + next_letter + next_two_letter)
                i += 2

            # Check if slice is a diphthong or umlaut case.
            elif ((
                letter in self.__open_vowels
                and next_letter in self.__closed_vowels
                and not letter in self.__accented_vowels
            ) or (
                letter in self.__closed_vowels
                and next_letter in self.__open_vowels
                and not letter in self.__accented_vowels
            ) or (
                letter in self.__umlauts
                and letter in self.__vowels
            ) or (letter in "uU" and next_letter in "iI") or (letter in "uU" and next_letter in "eE")):
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
        Returns tonic syllable string.
        """
        return self.syllables[self.__get_tonic_syllable_by_index()]

    def __get_tonic_syllable_by_index(self) -> int:
        """
        Returns tonic syllable index.
        """
        syllables_len = len(self.syllables)

        last_syllable = self.syllables[syllables_len -
                                       1] if syllables_len - 1 >= 0 else ""
        last_letter_in_last_syllable = last_syllable[len(
            last_syllable) - 1] if len(last_syllable) - 1 >= 0 else ""

        if (
            last_letter_in_last_syllable in self.__case_consonants
            and last_letter_in_last_syllable in self.__vowels
        ):
            tonic_index = syllables_len - 2 if syllables_len - 2 >= 0 else -1
        else:
            tonic_index = syllables_len - 1 if syllables_len - 1 >= 0 else -1

        for i, syllable in enumerate(self.syllables):
            for letter in syllable:
                if letter in self.__accented_vowels:
                    tonic_index = i

        return tonic_index

    def __get_vowels(self) -> list:
        """
        Returns all vowels of the word.
        """
        return [letter for letter in self.__word if has_vowels(letter)]

    def __get_consonants(self) -> list:
        """
        Returns all consonants of the word.
        """
        return [letter for letter in self.__word if has_consonants(letter)]

    def __get_type(self) -> int:
        """
        Returns a word type based on its grammatical classification.

        The values tha may be return are:
        -> 1 = Oxytone
        -> 2 = Paroxytone
        -> 3 = Proparoxytone
        -> 4 = Superproparoxytone
        """
        return (self.__get_tonic_syllable_by_index() - len(self.syllables)) * -1

    def __str__(self):
        return self.__word
