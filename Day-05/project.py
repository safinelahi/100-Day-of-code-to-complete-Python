# Password Generate Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers then the password might look like this: fgdx$*924

password = ""

for char in range(0 , nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(numbers)
for char in range(0, nr_numbers):
    password += random.choice(symbols)

print(f"Your easy password is: {password}")


# Hard Version
# When you've completed the easy version, you're ready to tackle the hard version.
# In the advanced version of this project the final password does not follow a pattern.
# So the example above might look like this: x$d24g*f9

password_list = []

for char in range(0 , nr_letters):
    password_list.append((random.choice(letters)))
for char in range(0, nr_symbols):
    password_list.append((random.choice(symbols)))
for char in range(0, nr_numbers):
    password_list.append((random.choice(numbers)))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your hard password is: {password}")