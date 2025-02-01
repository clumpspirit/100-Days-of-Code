import random
from os import system
from art import logo

def hit():
    """Returns a random item from cards list"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def score(cards):
    """Returns sum of integers in list, returns 0 if already at blackjack"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Ace will count as 1 if over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    total = sum(cards)
    return total

def compare(u_score, c_score):
    """Compares scores and returns winner"""
    if u_score == c_score:
        return "Push"

    elif c_score == 0:
        return "You lost."

    elif u_score == 0:
        return "You win."

    elif u_score > 21:
        return "You went over & lose."

    elif c_score > 21:
        return "Computer went over & you win."

    elif u_score > c_score:
        return "You win."

    else:
        return "You lose."

play_now = input("Would you like to play blackjack? y/n: ")

while play_now == 'y':
    system('clear')
    print(logo)

    my_hand = []
    computer_hand = []
    computer_score = 1337
    user_score = 1337

    for n in range(2):
        my_hand.append(hit())
        computer_hand.append(hit())

    user_turn = True
    while user_turn:

        user_score = score(my_hand)
        computer_score = score(computer_hand)
        print(f"Your cards: {my_hand}, current score: {user_score}")
        print(f"Computer hand: {computer_hand[0]}")

        if user_score == 0 or computer_hand == 0 or user_score > 21:
            user_turn = False

        else:
            hit_or_stay = input("Type 'y' to hit, type 'n' to stay: ")
            if hit_or_stay == 'y':
                my_hand.append(hit())
            else:
                user_turn = False

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(hit())
        computer_score = score(computer_hand)

    print(f"\nYour final hand: {my_hand}, final score: {user_score}")
    print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # Prompt to play again, if not 'y' then end loop
    play_now = input("Would you like to play blackjack? y/n: ")
