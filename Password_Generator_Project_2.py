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
  password += random.choice(letters)  #adds random letters to the password list nr_letter times
for _ in range (nr_symbols):
  password += random.choice(symbols)   #adds random symbols to the password list nr_letter times
for _ in range (nr_numbers):
  password += random.choice(numbers)   #adds random numbers to the password list nr_letter times

'''extracting all list entries out of the list'''

password = "".join(password)#password is changed from a list of strings to a string.

print (f"Your new password is:{new_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = [] #creates an empy list, that the password characters will be stored in.
for _ in range (nr_letters):
  password += random.choice(letters)  #adds random letters to the password list nr_letter times
for _ in range (nr_symbols):
  password += random.choice(symbols)   #adds random symbols to the password list nr_letter times
for _ in range (nr_numbers):
  password += random.choice(numbers)   #adds random numbers to the password list nr_letter times

'''extracting all list entries out of the list in randomized order'''

random.shuffle(password)
password = "".join(password) #password is changed from a list of strings to a string.
  
print (f"Your new random password is:{new_password}")
