x = 10

if x < 5:
    print("x is minor than 5")
elif x < 15:
    print("x is minor than 15")
else:
    print("x is greather than 15")

age = int(input("Please, enter your age: "))
if age <= 0:
    print("Enter a valid age")
elif age < 18:
    print("You are ilegal")
elif age > 65:
    print("It's time to die")
else:
    print("Hands up fucking idiot!")