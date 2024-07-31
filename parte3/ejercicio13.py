person = {
    "name": "Marcelo",
    "age": 26,
    "city": "San Nicolás de los Arroyos"
}

profile = person
# print(profile["age"])

people = {
    "person1": {
        "name": "Marcelo",
        "age": 26,
        "city": "San Nicolás de los Arroyos"
    },
    "person2": {
        "name": "Julieta",
        "age": 34,
        "city": "Rosario"
    },
    "person3": {
        "name": "Nicolás",
        "age": 30,
        "city": "Pergamino"
    },
}

data1 = people["person1"]
data2 = people["person2"]
data3 = people["person3"]

print(data1["name"])
print(data2["age"])
print(data3["city"])

person_to_complete = {
    "name": None,
    "age": None,
    "address": None,
    "phone": None
}

person_to_complete["name"] = input("Enter your name: ")
person_to_complete["age"] = input("Enter your age: ")
person_to_complete["address"] = input("Enter your address: ")
person_to_complete["phone"] = input("Enter your phone number: ")

print(person_to_complete)
