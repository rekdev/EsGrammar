from .utils import has_vowel, has_consonant, is_consonant_group

class Syllable:
    """
    This class contains varius methods from process words and get its syllables info.
    """

    def __init__(self, word: str):
        self.word = word
        self.vowels = "aeiouáéíóú"
        self.accented_vowels = "áéíóú"
        self.open_vowels = "aeoáéó"
        self.closed_vowels = "iuíú"

    def is_triphthong(self, x: str) -> bool:
        """
        Check if text slice is a triphthong.
        """
        open_vowels = self.open_vowels
        closed_vowels = self.closed_vowels
        x = x.lower()

        is_tp = False

        if len(x) == 3:
            is_tp = ((
                x[0] in closed_vowels
                and x[1] in open_vowels
                and x[2] in closed_vowels
            )
                or (
                x[0] in open_vowels
                and x[1] in closed_vowels
                and x[2] in open_vowels
            ))

        return is_tp

    def is_diphthong(self, x: str) -> bool:
        """
        Check if text slice is a diphthong.
        """
        open_vowels = self.open_vowels
        closed_vowels = self.closed_vowels
        accented_vowels = self.accented_vowels
        x = x.lower()

        is_dp = False

        if len(x) == 2:
            is_dp = (((
                x[0] in open_vowels
                and x[1] in closed_vowels
            )
                or (
                x[0] in closed_vowels
                and x[1] in open_vowels
            ))
                and not (x[0] in accented_vowels or x[1] in accented_vowels)
            )

        return is_dp

    def merge_vowels(self) -> list:
        """
        Take word and merge its vowels if not contains strong cases (hiatos).
        """
        word = self.word
        word_lenght = len(word)
        count = 0
        merged_vowels = []

        while count < word_lenght:
            letter = word[count]
            next_letter = word[count + 1] if count + 1 < word_lenght else ""
            next_letter2 = word[count + 2] if count + 2 < word_lenght else ""

            if self.is_triphthong(letter + next_letter + next_letter2):
                merged_vowels.append(letter + next_letter + next_letter2)
                count += 2

            elif self.is_diphthong(letter + next_letter):
                merged_vowels.append(letter + next_letter)
                count += 1

            else:
                merged_vowels.append(letter)

            count += 1

        return merged_vowels

    def get_syllables(self) -> list:
        """
        Split a word in syllables and return its syllable list.
        """
        merged_vowels = self.merge_vowels()
        merged_vowels_lenght = len(merged_vowels)
        syllables = []
        consonants_count = 0
        count = 0

        while count < merged_vowels_lenght:
            tmp_slice = merged_vowels[count]
            next_slice = merged_vowels[count + 1] if count + \
                1 < merged_vowels_lenght else ""
            prev_slice = merged_vowels[count - 1] if count - 1 >= 0 else ""

            if has_consonant(tmp_slice):
                consonants_count += 1

            # Check the syllable cases and make the syllable.
            if consonants_count == 1 and has_vowel(next_slice):
                tmp_slice += next_slice
                count += 1
                consonants_count = 0

            elif (
                consonants_count == 1
                and not is_consonant_group(tmp_slice + next_slice)
                and (has_consonant(next_slice) or next_slice == "")
            ):

                syllables_lenght = len(syllables)

                if syllables_lenght > 0:
                    syllables[syllables_lenght - 1] += tmp_slice

                consonants_count = 0

            elif (
                consonants_count == 2
                and is_consonant_group(prev_slice + tmp_slice)
                and has_vowel(next_slice)
            ):

                tmp_slice = prev_slice + tmp_slice + next_slice
                count += 1
                consonants_count = 0

            # Assing temporal slice into syllable var and append the result.
            syllable = tmp_slice

            if (
                syllable != ""
                and not (len(syllable) == 1
                         and has_consonant(syllable))
            ):

                syllables.append(syllable)

            count += 1

        return syllables

        def get_tone_syllable():
            """
            """
            pass
