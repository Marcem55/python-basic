number = int(input("Please, enter an integer number: "))

match number:
    case number if number < 0:
        print("El numero se encuentra en el rango 1")
    case number if number >= 0 and number < 10:
        print("El numero se encuentra en el rango 2")
    case number if number >= 10:
        print("El numero se encuentra en el rango 3")
    case _:
        print("Rango desconocido")
