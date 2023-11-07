from es_grammar import Category

word = str(input("Ingrese una palabra: "))

ct = Category(word)

print(ct.categorize())