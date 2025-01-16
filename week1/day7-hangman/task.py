import random
import hangman_art
import hangman_words

print(hangman_art.logo)
# Choose random word from list
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

# Create placeholder
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

# Create list to hold progress towards word
correct_letters = []

# Create game over boolean for while loop
game_over = False

# Create lives and ascii list counter
lives = 6
ascii_stage = 0

# Print graphic and word length
print(hangman_art.ascii[ascii_stage])
print(placeholder)

while game_over == False:
    guess = input("\nGuess a letter: \n").lower()
    display = ""

    # Check if they already guessed the letter
    if guess in correct_letters:
        print(f"You already guessed {guess}.")

    # Check if the guessed letter is in the word
    for letter in chosen_word:
        if guess == letter:
            display += letter 
            correct_letters.append(letter)

        # Redisplay letter if it's in the correct guesses already
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Subtract a life if guess is wrong
    if guess not in chosen_word:
        lives -= 1
        ascii_stage += 1
        print(f"Lives left: {lives}")

    print(f"\n{hangman_art.ascii[ascii_stage]}\n{display}")

    # Check if any "_" are left
    if "_" not in display:
        game_over = True
        print("\n**You win.**")

    # Check if lives left
    if lives == 0:
        game_over = True
        print(f"\n**You lose.**\nCorrect word was {chosen_word}.")
