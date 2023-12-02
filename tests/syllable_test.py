from esgrammar import Syllable

words = [
    "Vío",
    "Árbol",
    "Tríptico",
    "Poesía",
    "Período",
    "Saúco",
    "Murciélago",
    "Zoologico",
    "Aéreo",
    "Leer",
    "Período",
    "Abreviáis",
    "Anunciéis",
    "Miau",
    "Buey",
    "Uruguay",
    "Queso",
    "Paisaje",
    "Peine",
    "Estadounidense",
    "Álgebra",
    "Platano",
    "Computadora",
    "Llanta",
    "Perro",
    "Gato",
    "Cabra",
    "Pollo",
    "Eduardo",
    "Pingüino",
    "Vergüenza",
    "Águila",
    "Guitarra",
    "Gratuito",
    "Constituís"
]
words_syllables = [
    ["Ví", "o"],
    ["Ár", "bol"],
    ["Tríp", "ti", "co"],
    ["Po", "e", "sí", "a"],
    ["Pe", "rí", "o", "do"],
    ["Sa", "ú", "co"],
    ["Mur", "ci", "é", "la", "go"],
    ["Zo", "o", "lo", "gi", "co"],
    ["A", "é", "re", "o"],
    ["Le", "er"],
    ["Pe", "rí", "o", "do"],
    ["A", "bre", "viáis"],
    ["A", "nun", "ciéis"],
    ["Miau"],
    ["Buey"],
    ["U", "ru", "guay"],
    ["Que", "so"],
    ["Pai", "sa", "je"],
    ["Pei", "ne"],
    ["Es", "ta", "dou", "ni", "den", "se"],
    ["Ál", "ge", "bra"],
    ["Pla", "ta", "no"],
    ["Com", "pu", "ta", "do", "ra"],
    ["Llan", "ta"],
    ["Pe", "rro"],
    ["Ga", "to"],
    ["Ca", "bra"],
    ["Po", "llo"],
    ["E", "duar", "do"],
    ["Pin", "güi", "no"],
    ["Ver", "güen", "za"],
    ["Á", "gui", "la"],
    ["Gui", "ta", "rra"],
    ["Gra", "tui", "to"],
    ["Cons", "ti", "tuís"]
]


def test_syllable():
    words_lenght = len(words)

    for i in range(0, words_lenght):
        slb = Syllable(words[i])

        word_test = slb.get_syllables()
        word_syllable = words_syllables[i]

        assert word_test == word_syllable
