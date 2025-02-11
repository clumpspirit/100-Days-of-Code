import coffee

def check_resource(ordered_ingredients):
    """Checks if there are enough resources"""
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= coffee.resources[item]:
            print(f"Sorry there is not enough of {item}")
            return False
    return True

def process_coins():
    """Returns the total calculation of coins"""
    print("Insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    """Checks if transaction is successful"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money. Money refunded.")
        return False

def make_coffee(chosen_drink, ordered_ingredients):
    """Deducts resources"""
    for item in ordered_ingredients:
        coffee.resources[item] -= ordered_ingredients[item]
    print(f"Here is your {chosen_drink}")

water = coffee.resources["water"]
milk = coffee.resources["milk"]
coffee_resource = coffee.resources["coffee"]
profit = 0.0

prompt = True
while prompt == True:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        prompt = False
    elif choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee_resource}g\nMoney: ${profit}")
    else:
        drink = coffee.MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
