#1 Pide al usuario su edad y comprueba si es mayor de edad (18 años).
# edad = 18
# pedir_edad = int(input("Digame su edad: "))
# if pedir_edad < edad:
#     print("Menor de edad")
# else:
#     print("Mayor de edad")

#2 Declara una lista con los números del 1 al 10 y comprueba si un número ingresado por el usuario está en la lista.
# numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# pedir_numero = int(input("Numero: "))
# if pedir_numero in numeros:
#     print("OH YEAH")
# else:
#     print("WOO WOO")


#3 Pide al usuario un número y comprueba si es par.
# numero = int(input("Numero: "))
# if numero % 2 == 0:
#     print("Par")


#4 Declara una lista con los días de la semana y comprueba si un día ingresado por el usuario es fin de semana.
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# user_day = input("Enter a day: ")
# if user_day in days and user_day == "Saturday" or user_day == "Sunday":
#     print("It's weekend! Let's drink some beers!")
# else:
#     print("Booooriiiiing")



#5 Pide al usuario su nombre y comprueba si tiene más de 5 letras.
# user_name = input("Enter your name: ")
# name_long = len(user_name)
# if name_long > 5:
#     print("More than 5 letters")
# else:
#     print("Less than 5 letters")


#6 Declara una lista con los números del 1 al 20 y comprueba si un número ingresado por el usuario está en la lista y es par o impar. (usar template strings)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# user_number = int(input("Ingresa un numero del 1 al 20: "))
# if not user_number in numbers:
#     print("Number not founded")
# else:
#     number_rest = user_number % 2
#     if number_rest != 0:
#         print(f"{user_number} founded and is even")
#     else:
#         print(f"{user_number} founded and is odd")


#7 Pide al usuario un número y comprueba si es múltiplo de 3 o 5.
# user_number = int(input("Enter an integer number: "))

# if user_number % 3 == 0 and user_number % 5 == 0:
#     print("Multiple of 3 and 5")
# elif user_number % 3 == 0 and user_number % 5 != 0:
#     print("Multiple of 3")
# elif user_number % 3 != 0 and user_number % 5 == 0:
#     print("Multiple of 5")
# else:
#     print("Multiple of your ass")


#8 Declara una lista con los meses del año y comprueba si un mes ingresado por el usuario tiene 30 días.
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# user_month = input("Enter a month: ")
# if not user_month in months:
#     print("Wrong month")

# match user_month:
#     case "January":
#         print("31 days")
#     case "February":
#         print("28 days")
#     case "March":
#         print("31 days")
#     case "April":
#         print("30 days")
#     case "May":
#         print("31 days")
#     case "June":
#         print("30 days")
#     case "July":
#         print("31 days")
#     case "August":
#         print("31 days")
#     case "September":
#         print("30 days")
#     case "October":
#         print("31 days")
#     case "November":
#         print("30 days")
#     case "December":
#         print("31 days")
    



#9 Pide al usuario su edad y comprueba si es mayor de edad y tiene más de 5 letras en su nombre.
# user_name = input("What's your name? ")
# user_age = int(input("How old are you? "))
# legal = user_age >= 18
# if legal:
#     print(f"{user_name}, you are legal and your name has {len(user_name)} letters")
# else:
#     print(f"{user_name}, you are ilegal and your name has {len(user_name)} letters")


#10 Declara una lista con los números del 1 al 50 y comprueba si un número ingresado por el usuario está en la lista y es par.



#11 Pide al usuario un número y comprueba si es un número perfecto (la suma de sus divisores es igual al número).
# user_number = int(input("Enter a number: "))
# if user_number == 1:
#     print("1 is perfect")
# else:
#     divisor_sum = 0
#     aux_num = user_number - 1

#     while aux_num > 0:
#         if user_number % aux_num != 0:
#             aux_num -= 1
#         else:
#             divisor_sum = divisor_sum + aux_num
#             aux_num -= 1

#     if user_number == divisor_sum:
#         print(f"{user_number} is perfect")
#     else:
#         print(f"{user_number} is not perfect")


#12 Declara una lista con colores y comprueba si un color ingresado por el usuario está en la lista.
colors = ["red", "blue", "yellow", "pink", "white", "black", "orange"]
user_color = input("Enter a color: ")
if user_color in colors:
    print("It's in the list")
else:
    print("It isn't in the list")


#13 Pide al usuario su nombre y comprueba si tiene más de 3 vocales.



#14 Declara una lista con los números del 1 al 100 y comprueba si un número ingresado por el usuario es un cuadrado perfecto.



#15 Pide al usuario un número y comprueba si es un número armónico (la suma de sus divisores es igual a 1).



#16 Declara una lista con los países de América y comprueba si un país ingresado por el usuario está en la lista.



#17 Pide al usuario su edad y comprueba si es mayor de edad y tiene más de 2 consonantes en su nombre.



#18 Declara una lista con los números del 1 al 200 y comprueba si un número ingresado por el usuario está en la lista y es impar.



#19 Pide al usuario un número y comprueba si es un número triangular (la suma de los números naturales hasta ese número es igual al número).



#20 Declara una lista con los personajes de una serie y comprueba si un personaje ingresado por el usuario está en la lista y tiene más de 5 letras en su nombre.


