rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps_bag = [rock, paper, scissors]#puts all the art in a bag that's easy to reference.
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
player_rps_choice = rps_bag[player_choice] #Allocates the players choice with a value in rps_bag.
computer_rps_choice = rps_bag[computer_choice] #Allocates the computers random choice with a value in rps_bag.
sort_list = [scissors, rock, paper, scissors]#makes a "never ending" list that allows scissors to be beaten by rock but also beat paper when referenced with index.
sort_list_index_player = sort_list.index(player_rps_choice, 1, 4) #Players sort_list starts at rock(1), so that computer can be asked if it has a lower index. 
sort_list_index_computer = sort_list.index(computer_rps_choice, 0, 4)

### Game Output

print(player_rps_choice)
print("Computer chose:" + computer_rps_choice)

### Logic

if sort_list_index_computer == sort_list_index_player-1 :
  print("You win!")
elif player_rps_choice == computer_rps_choice :
  print("It's a tie!")
else :
  print("You lose!")



