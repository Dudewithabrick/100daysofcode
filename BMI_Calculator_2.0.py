# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = round(weight / height**2)
## with Bold diagnose
#if BMI < 18.5:
#    diagnose = "are \033[1munderweight\033[0m"
#elif BMI < 25:
#    diagnose = "have a \033[1mnormal weight\033[0m"
#elif BMI < 30:
#    diagnose = "are \033[1mslightly overweight\033[0m"
#elif BMI < 35:
#    diagnose = "are \033[1mobese\033[0m"
#else:
#    diagnose = "are \033[1mclinically obese\033[0m"
## without bold diagnose
if BMI < 18.5:
    diagnose = "are underweight"
elif BMI < 25:
    diagnose = "have a normal weight"
elif BMI < 30:
    diagnose = "are slightly overweight"
elif BMI < 35:
    diagnose = "are obese"
else:
    diagnose = "are clinically obese"

print(f"Your BMI is {BMI}, you {diagnose}.")
