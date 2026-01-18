#You are going to build a Rock, Paper, Scissors game.
# You will need to use what you have learnt about randomization and Lists to achieve this.

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
import random
games_items = [rock, paper, scissors]

print("Welcome the Rock, Paper, Scissors game")
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choose >= 0 or user_choose <= 2:
    print(games_items[user_choose])

computer_choose = random.randint(0,2)
print("Computer chose:")
print(games_items[computer_choose])

if user_choose < 0 or computer_choose >= 3:
    print("You typed an invalid number. You lose!")
elif user_choose == computer_choose:
    print("It's a draw!")
elif user_choose == 0 and computer_choose == 2:
    print("You win!")
elif computer_choose == 0 and user_choose == 2:
    print("You lose!")
elif user_choose > computer_choose:
    print("You win!")
elif computer_choose > user_choose:
    print("You lose!")