number = 4

### MATCH --> Es como el switch en javascript

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Unknown number")

number2 = int(input("Please, enter an integer number: "))
match number2:
    case 0:
        print("Do not enter 0, idiot!")
    case number2 if number2 % 2 == 0:
        print("Even number")
    case number2 if number2 % 2 != 0:
        print("Odd number")
    case _:
        print("Unknown number")