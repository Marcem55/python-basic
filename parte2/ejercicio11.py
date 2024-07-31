### TUPLAS --> Tipos de datos parecido a arrays, solo que no se pueden modificar.

tupla_numbers = (1, 2, 3)

tupla_strings = ("apple", "banana", "cherry")

tupla_mix = (4, "hello", 3.1416)

tupla_empty = ()

print(tupla_numbers[0])
print(tupla_strings[1])
print(tupla_mix[2])

people = (("Juli", 34), ("Kikin", 40), ("Pibito", 15), ("Belofornite", 30))

for name, age in people:
    if age >= 18:
        print(name, age)


numbers = (10, 20, 30, 40, 50, 100, 5000, 100)

sum = sum(numbers)
print(f"The result is {sum}")
