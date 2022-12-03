# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name = name1.lower()+name2.lower()
amount_true = lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") + lower_case_name.count("e")
amount_love = lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") + lower_case_name.count("e")
compatibility_score = str(amount_true) + str(amount_love)
compatibility_score = int(compatibility_score)

if compatibility_score < 10 or compatibility_score > 90 :
    print(f"Your score is {compatibility_score}, you go together like coke and mentos.")
elif compatibility_score > 40 and compatibility_score < 50 : 
    print(f"Your score is {compatibility_score}, you are alright together.")
else :
    print(f"Your score is {compatibility_score}.")

