name = "Marcelo"
last_name = "Malacalza"
phrase = "Hay que comer lo que hay"

length = len(phrase)
print(length)

print(last_name[0])

words = phrase.split()
print(words)

upper = name.upper()
print(upper)

lower_last_name = last_name.lower()
print(lower_last_name)

message = "Hello World"
changed_message = message.replace("Hello", "Big")
print(changed_message)

for letter in last_name:
    print(letter)
