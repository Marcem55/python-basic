words = ("manzana", "banana", "auto", "fernet", "fortnite")

search_word = input("Por favor, ingresa una palabra: ")

if words.__contains__(search_word):
    print("La palabra está en la tupla")
else:
    print("La palabra no está en la tupla")