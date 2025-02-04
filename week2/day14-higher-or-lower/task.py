import game_data
import art
import random

def person(new_person):
    """Creates a new list based on a random person from the data"""
    random_number = random.randint(0, len(game_data.data) - 1)
    name = game_data.data[random_number]["name"]
    follower_count = game_data.data[random_number]["follower_count"]
    description = game_data.data[random_number]["description"]
    country = game_data.data[random_number]["country"]
    new_person.append(name)
    new_person.append(follower_count)
    new_person.append(description)
    new_person.append(country)

# Print inital logo and starting person. The starting person is only needed at the beginning.
print(art.logo)
initial_person = []
person(initial_person)
score = 0

in_game = True
while in_game:

    # Fetch new person data
    new_person = []
    person(new_person)

    print(f"Compare A: {initial_person[0]}, a {initial_person[2]}, from {initial_person[3]}")
    print(f"Against B: {new_person[0]}, a {new_person[2]}, from {new_person[3]}")

    if initial_person == new_person:
        # If the people are the same, make sure they're not.
        person(new_person)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # If you pick A and A > B
    if guess == 'A' and initial_person[1] > new_person[1]:
        score += 1
        print(art.logo)
        print(f"Correct. Current score: {score}")
        initial_person = new_person
    # If you pick B and B > A
    elif guess == 'B' and new_person[1] > initial_person[1]:
        score += 1
        print(art.logo)
        print(f"Correct. Current score: {score}")
        initial_person = new_person
    else:
        print(f"Wrong guess. Your score was {score}.")
        in_game = False
