#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = [] #creates an empy list, that the password characters will be stored in.
for _ in range (nr_letters):
  password.append(letters[random.randint(0,51)])  #adds random letters to the password list nr_letter times
for _ in range (nr_symbols):
  password.append(symbols[random.randint(0,8)])   #adds random symbols to the password list nr_letter times
for _ in range (nr_numbers):
  password.append(numbers[random.randint(0,9)])   #adds random numbers to the password list nr_letter times

'''extracting all list entries out of the list'''
new_password = ""
for i in range (0, len(password)):
  new_password += f"{password[i]}"

print (f"Your new password is:{new_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
for _ in range (nr_letters):
  password.append(letters[random.randint(0,51)])  #adds random letters to the password list nr_letter times
for _ in range (nr_symbols):
  password.append(symbols[random.randint(0,8)])   #adds random symbols to the password list nr_letter times
for _ in range (nr_numbers):
  password.append(numbers[random.randint(0,9)])   #adds random numbers to the password list nr_letter times

'''extracting all list entries out of the list in randomized order'''

new_password = ""
for _ in range (len(password)):
  character_position = random.randint(0, len(password)-1)
  new_password += f"{password[character_position]}"
  password.pop(character_position)
  
print (f"Your new random password is:{new_password}")
