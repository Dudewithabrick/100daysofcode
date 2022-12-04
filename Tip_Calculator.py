#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Intro
print("Welcome to the tip calculator.")
#Variables
total_bill = float(input("What was the total bill? €"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_num = int(input("How many people to split the bill? "))
#Calculation
total_bill_including_tip = total_bill * (tip_percentage / 100 + 1)
split_amount = total_bill_including_tip / people_num
split_amount = "{:.2f}".format(round(split_amount)) #format into string with 2 decimal points
#Answer
print(f"Each person should pay: €{split_amount}")