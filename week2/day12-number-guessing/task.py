import random
from art import logo

def set_difficulty():
    """Set difficulty globally when called"""
    global difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def check_number(user_guess, rng, turns):
    """Returns if number is higher or lower and takes away a life if it is"""
    if user_guess < rng:
        print("Too low.")
        return turns - 1

    elif user_guess > rng:
        print("Too high.")
        return turns - 1

    else:
        print(f"You win. The number was {rng}.")
        return

# Generate random number between 1 and 100 including
random_num = random.randint(1, 100)

print(logo)
print("Welcome to the numbers game.\nI'm thinking of a number between 1-100.")
print(random_num)

# Set amount of lives
set_difficulty()
if difficulty == "hard":
    lives = 5
elif difficulty == "easy":
    lives = 10
else:
    print(f"No difficulty: {difficulty}")


# Loop game
in_game = True
while in_game and lives > 0:

    print(f"Lives: {lives}")
    guess = int(input("Make a guess: "))

    lives = check_number(guess, random_num, lives)

    # Check if correct guess break loop
    if guess == random_num:
        in_game = False

if lives == 0:
    print("Out of lives, game over.")
