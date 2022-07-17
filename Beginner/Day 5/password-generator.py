#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_password = ""

for i in range(nr_letters):
    easy_password += random.choice(letters)

for i in range(nr_symbols):
    easy_password += random.choice(symbols)

for i in range(nr_numbers):
    easy_password += random.choice(numbers)

print("Easy Password: ",easy_password)

# Creating random sequence of easy password
characters = []
for char in easy_password:
    characters.append(char)
hard_password = ""
random.shuffle(characters)
for char in characters:
    hard_password += char
print("Hard Password: ",hard_password)
