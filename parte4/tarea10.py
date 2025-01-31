# Crea una clase llamada ContadorPalabras que tenga los siguientes métodos:

#     __init__: El constructor que inicializa un atributo contador en 0.

#     contar: Un método que toma una cadena de texto como argumento y cuenta cuántas palabras contiene esa cadena. Debe incrementar el contador en la cantidad de palabras encontradas.

#      obtener_contador: Un método que devuelve el valor actual del contador.

# A continuación, crea una instancia de la clase ContadorPalabras, utiliza el método contar para contar palabras en una cadena de texto y luego muestra el resultado utilizando el método obtener_contador.

class ContadorPalabras:
    def __init__(self, num):
        self.contador = num

    def contar(self, cadena):
        palabras = cadena.split()
        self.contador += len(palabras)

    def obtener_contador(self):
        return self.contador

nuevo_contador = ContadorPalabras(0)
nuevo_contador.contar("Hola, me llamo Luis")

print(nuevo_contador.obtener_contador())