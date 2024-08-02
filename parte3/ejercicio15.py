import module1

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a 2nd number: "))

sum = module1.sum(num1, num2)
substract = module1.substract(num1, num2)
multiply = module1.multiply(num1, num2)
division = module1.division(num1, num2)

print("+:", sum, "-:", substract, "*:", multiply, "/:", division)