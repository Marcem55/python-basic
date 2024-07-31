fruits = ["apple", "banana", "cherry", "orange"]
counter = 0

## FOR LOOPS

for fruit in fruits:
    counter += 1
    print(f"fruit #{counter}: {fruit}")
    if fruit == "cherry":
        break

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    square = number ** 2
    print(f"The {number}'s square is {square}")
