def calculator(num1, num2, op):
    return eval(f"{num1} {op} {num2}")
    # match op:
    #     case "+":
    #         return num1 + num2
    #     case "-":
    #         return num1 - num2
    #     case "/":
    #         return num1 / num2
    #     case "*":
    #         return num1 * num2
    #     case _:
    #         return "Invalid operation"
        
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a 2nd number: "))
operation = input("Enter an operation: ")
print(calculator(number1, number2, operation))