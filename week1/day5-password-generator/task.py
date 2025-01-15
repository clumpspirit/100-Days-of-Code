#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""

# For every letter, symbol, and number in the range of 0 to whatever the user picks, add a random choice from respective list
for letter in range(0, nr_letters):
    rand_letters = random.choice(letters)
    easy_password = easy_password + rand_letters

for symbol in range(0, nr_symbols):
    rand_symbols = random.choice(symbols)
    easy_password = easy_password + rand_symbols

for number in range(0, nr_numbers):
    rand_numbers = str(random.choice(numbers))
    easy_password = easy_password + rand_numbers

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Randomly pick from easy_password
hard_password = random.sample(easy_password, len(easy_password))

# The above sample function returns a list, join the list contents into a string
print(''.join(hard_password))





