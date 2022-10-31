import random

letter_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_bank = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_bank = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Welcome to the PyPassword Generator! Please use this tool to create a secure \npassword. Please keep in mind that new password should be used for each site.")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print('\n')

user_letters= int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))


for x in range(1, user_letters + 1):
    password.append(random.choice(letter_bank))

for x in range(1, user_symbols + 1):
  password += random.choice(symbol_bank)

for x in range(1, user_numbers + 1):
  password += random.choice(number_bank)

final_password = ""
for y in password:
  final_password += y

print(f"Your password is: {final_password}")
