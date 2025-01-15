print("Welcome to the tip calculator.\n")

# Store bill in float
bill = float(input("What was the total of the bill?\n$"))

# Convert percentage to float and divide by 100 to get decimal
tip_percentage = (float(input("How much would you like to tip? (10, 12, 15)\n")) / 100)

# Store size of group in integer
group_count = int(input("How many people splitting the total?\n"))

# Add tip to bill
bill_with_tip = bill + (bill * tip_percentage) 

# Round bill split per person to second decimal place
total_per_person = round(bill_with_tip / group_count, 2)

print(f"Each person should pay ${total_per_person}")
