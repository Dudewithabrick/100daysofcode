# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#turn age into int

age = int(age)

#calculate how old the person is in days, weeks & months

days_alive = 365 * age
weeks_alive = 52 * age
months_alive = 12 * age

#calculate how many days, weeks & months are in 90 years

days_90 = 365 * 90
weeks_90 = 52 * 90
months_90 = 12 * 90

#Calculate how many days, weeks & months are left until 90 years old

days_left = days_90 - days_alive
weeks_left = weeks_90 - weeks_alive
months_left = months_90 - months_alive

#print answer

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


