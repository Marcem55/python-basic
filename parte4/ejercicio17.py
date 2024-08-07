class Calculator1:
    def __init__(self, number):
        self.result = number

    def sum(self, number):
        self.result += number
    
    def substract(self, number):
        self.result -= number

    def multiply(self, number):
        self.result *= number

    def division(self, number):
        if number == 0:
            print("Error: Cannot divide between 0")
        else:
            self.result /= number

    def result(self):
        return self.result
    
calc = Calculator1(0)
calc.sum(5)
calc.multiply(4)
calc.substract(5)
calc.division(2)
print(calc.result)

class Calculator2:
    def sum(self, num1, num2):
        return num1 + num2
    
    def substract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            print("Error: Cannot divide between 0")
        else:
            return num1 / num2

    def result(self):
        return self.result
    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a 2nd number: "))
calc2 = Calculator2()
sum2 = calc2.sum(num1, num2)
mult2 = calc2.multiply(num1, num2)
subst2 = calc2.substract(num1, num2)
div2 = calc2.division(num1, num2)
print(sum2, subst2, mult2, div2)
