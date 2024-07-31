# METODOS PARA LISTAS

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
my_list = [5, "Marcem55", 55, "Tu culo en llamas", True]

print(numbers[0])
print(fruits[2])

numbers[4] = 55
print("numbers after change", numbers)

numbers.append(99)
print("numbers after append", numbers)

fruits.append("orange")
print("fruits after append", fruits)

del numbers[2]
print("numbers after del", numbers)
del fruits[0]
print("fruits after del", fruits)

for fruit in fruits:
    print(fruit)

result_sum = sum(numbers)
print(result_sum)
