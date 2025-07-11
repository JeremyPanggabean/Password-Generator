import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# Sequence Password
# Password = ""
#
# for char in range(0, nr_letters):
#     random_char = random.choice(letters)
#     Password += random_char
#
# for symbol in range(0, nr_symbols):
#     random_symbol = random.choice(symbols)
#     Password += random_symbol
#
# for number in range(0, nr_numbers):
#     random_number = random.choice(numbers)
#     Password += random_number
#
# print(f"Your Password in sequences is: {Password}")


## Random Password
Password_list = []

for char in range(0, nr_letters):
    Password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    Password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    Password_list.append(random.choice(numbers))

print(Password_list)
random.shuffle(Password_list)
print(Password_list)

# Password in String
Password = ""
for char in Password_list:
    Password += char

print(f"Your Password is: {Password}")