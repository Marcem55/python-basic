qualification = float(input("Ingresa tu calificación: "))

if qualification >= 90:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif qualification >= 70:
    print("Has aprobado satisfactoriamente.")
elif qualification >= 60:
    print("Has aprobado, pero necesitas mejorar un poco.")
else:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")