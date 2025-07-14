# Jermaine Furze
# 7/12/25
# P5LAB - Self Checkout Change Dispenser
# This program simulates a self-checkout machine that takes a random purchase total and user payment, 
# then calculates and displays the change in dollars and coins.

import random

# Function to break change down into coins and bills
def disperse_change(change):
    change_cents = round(change * 100)  # Convert dollars to cents

    # Dictionary to store denomination values in cents
    denominations = {
        "Dollars": 100,
        "Quarters": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennies": 1
    }

    print("\nChange to return: ${:.2f}".format(change))
    print("Dispensed as:")

    for name, value in denominations.items():
        count = change_cents // value
        change_cents %= value
        print(f"{name}: {count}")


# Main function
def main():
    # Generate a random total owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"\nTotal amount owed: ${amount_owed:.2f}")

    # Ask user to enter amount of cash inserted
    cash_given = float(input("Enter the amount of cash you are inserting: $"))

    # Ensure user gave enough money
    while cash_given < amount_owed:
        print("Insufficient amount. Please enter an amount equal to or greater than the amount owed.")
        cash_given = float(input("Enter the amount of cash you are inserting: $"))

    # Calculate change
    change = round(cash_given - amount_owed, 2)

    # Call function to show change
    disperse_change(change)

# Call main to run the program
main()
