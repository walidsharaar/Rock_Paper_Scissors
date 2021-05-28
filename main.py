# Project start
import random

print("Welcome to Rock Paper Scissor Game ! \n")

user_selection = int(input("Choose 1 for Rock, 2 for Paper or 3 for Scissors:\n"))

# variable defination

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

game_emojis=[rock,paper,scissors]

computer_selection= random.randint(1,3)

if user_selection ==0 and computer_selection=2:
    print("You win!")
elif computer_selection>user_selection:
    print("You Lose!")
else:
    ("Invalid Input, You Lose!")