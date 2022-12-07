# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
###Objective
#You are going to write a program that calculates the average student height from a List of heights.
#mportant You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#Write your code below this row 👇
sum_of_heights = 0
index = 0

for heights in student_heights:
    index += 1
    sum_of_heights += heights

average_height = sum_of_heights / index

print(round(average_height))


