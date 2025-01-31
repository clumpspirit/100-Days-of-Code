from os import system
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

symbols = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }


def calculator():
    """Returns an output of an operation of two numbers 
    based on the dictionary 'symbols' and the other functions in this document"""

    print(logo)
    n1 = float(input("Initial number: "))
    continue_answer = True
    while continue_answer:
        for item in symbols:
            print(item)
        operation = input("What would you like to do? ")
        n2 = float(input("Second number: "))

        result = symbols[operation](n1, n2)

        keep_going = input(f"{n1} {operation} {n2} = {result}\nWould you like to caluclating with {result}? (y/n): ").lower()


        if keep_going == "y":
            system('clear')
            n1 = result
            print(f"Result = {n1}")
        elif keep_going == "n":
            system('clear')
            continue_answer = False
            calculator()
        else:
            print("Type 'y' or 'n'")

# Call the function, otherwise code does nothing
calculator()
