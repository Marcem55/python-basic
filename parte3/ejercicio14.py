# FUNCTIONS --> def
# def sayHello(name):
#     print(f"Hello {name}")

# sayHello("Julieta fat lechon")

# def sum(a, b):
#     result = a + b
#     print(result)

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a 2nd number: "))
# result_sum = sum(num1, num2)
# print(result_sum)

# def isOdd(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# user_number = int(input("Enter a number to evaluate: "))
# if isOdd(user_number):
#     print("Is ODD")
# else:
#     print("Is EVEN")

def numberList(list):
    max_number = max(list)
    return max_number

print(numberList([5 , 987, 34, 6, 654, 654, 988, 36, 4]))
