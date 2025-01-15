print("Welcome to the pizza delivery service.\n")
size = input("What size pizza do you want? (S, M, or L) ")
mushroom = input("Do you want mushroom on your pizza? (Y or N) ")
extra_cheese = input("Do you want extra cheese? (Y or N) ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Wrong input.")

if mushroom == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total is: ${bill}")
