from os import system

# Find highest bid with corresponding winner in dictionary
def highest_bidder(dictionary):

    winner = ""
    high = 0

    for bidder in dictionary:
        if dictionary[bidder] > high:
            high = dictionary[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid amount of {high}! ")

bids = {}
loop = "YES"
# Loop while adding people and bids to dictionary
while loop == "YES":

    system("clear")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))

    bids[name] = bid

    loop = input("Would another person like to bid? Type yes or no. ").upper()


# Call the function to determine winner
highest_bidder(bids)


