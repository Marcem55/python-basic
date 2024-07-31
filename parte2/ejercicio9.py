## WHILE LOOP

counter = 1
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 6:
        break

newYear = 10
while newYear > 0:
    print(newYear)
    newYear -= 1

print("Happy new year!!!!")

sum = 0
number = int(input("Please, enter a positive number (or a negative number to leave): "))

while number >= 0:
    sum += number
    number = int(input("Please, enter a positive number (or a negative number to leave): "))

print(f"The result is {sum}")
