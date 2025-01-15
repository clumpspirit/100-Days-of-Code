import random

# Store ASCII art
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissors]

player_input = int(input("Welcome, what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if 0 <= player_input <= 2:
    print(f"Player chose\n{game[player_input]}")


computer_choice = random.randint(0, 2)
print(f"Computer chose\n{game[computer_choice]}")

# If player decides to be a funny guy
if player_input > 2 or player_input < 0:
    print("You lost by default. Pick 0, 1, or 2.")

# If player chooses rock and computer paper
elif player_input == 0 and computer_choice == 2:
    print("You win.")

# If player chooses scissors and computer rock
elif player_input == 2 and computer_choice == 0:
    print("You lose.")

# Catch if player chooses rock and computer paper and if player chooses paper and computer scissors
elif player_input < computer_choice:
    print("You lose.")

# Catch if player chooses paper and computer rock and if player chooses scissors and computer paper
elif player_input > computer_choice:
    print("You win.")

# If both players choose the same thing
elif player_input == computer_choice:
    print("Draw.")
