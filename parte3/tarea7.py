personal_data = {
    "name": None,
    "age": None,
    "address": None,
    "phone": None,
}

personal_data["name"] = input("Enter your name: ")
personal_data["age"] = input("Enter your age: ")
personal_data["address"] = input("Enter your address: ")
personal_data["phone"] = input("Enter your phone: ")

print(f"{personal_data['name']} is {personal_data['age']} years old, lives in {personal_data['address']} and his/her phone number is {personal_data['phone']}")