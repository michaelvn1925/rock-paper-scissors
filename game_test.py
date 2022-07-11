import random

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

game_image = [rock, paper, scissors]

user_choice = int(input("What do you chioose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3:
  print("You typed an invalid number.")
else:
print(game_image[user_choice])

comp_choice = random.randint(0, 2)
print(f"Computer choose {comp_choice}")
print(game_image[comp_choice])

if user_choice == 0 and comp_choice == 2:
  print("You Win!")
elif comp_choice == 0 and user_choice == 2:
  print("You lose!")
elif comp_choice > user_choice:
  print("You lose!")
elif user_choice == 1 and comp_choice == 0:
  print("You Win!")
elif comp_choice == user_choice:
  print("It's a Draw!")
