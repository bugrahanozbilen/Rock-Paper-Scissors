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

#Write your code below this line 👇

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer = str(random.randint(0, 2))


if player == "0":
  print(rock)
elif player == "1":
  print(paper)
elif player == "2":
  print(scissors)

if computer == "0":
  print(f"Computer choice:\n{(rock)}")
elif computer == "1":
  print(f"Computer choice:\n{(paper)}")
elif computer == "2":
  print(f"Computer choice:\n{(scissors)}")

if player == "0" and computer == "0":
  print("Draw!")
elif player == "1" and computer == "0":
  print("Player win!")
elif player == "2" and computer == "0":
  print("Computer win!")
elif player == "1" and computer == "1":
  print("Draw!")
elif player == "0" and computer == "1":
  print("Computer win!")
elif player == "2" and computer == "1":
  print("Player win!")
elif player == "0" and computer == "2":
  print("Player win!")
elif player == "1" and computer == "2":
  print("Computer win!")
elif player == "2" and computer == "2":
  print("Draw!")
else:
  print("Your input invalid. You loose!")