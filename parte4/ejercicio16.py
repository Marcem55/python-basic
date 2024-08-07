class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old")

# Crear una instancia de la clase Persona
person1 = Person("Marcelo", 26)

person1.sayHi()

person2 = Person("Julieta", 34)

person2.sayHi()