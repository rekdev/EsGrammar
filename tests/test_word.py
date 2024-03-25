import json
from esgrammar import Word


def test_word():
    words = json.load(open("tests/words.json"))

    for word_item in words:
        word = Word(word_item["word"])

        assert word.syllables == word_item["syllables"] \
               and word.tonic_syllable == word_item["tonic_syllable"] \
               and word.tonic_syllable_index == word_item["tonic_syllable_index"] \
               and word.vowels == word_item["vowels"] \
               and word.consonants == word_item["consonants"] \
               and word.type == word_item["type"] \
               and word.value == word_item["word"]
