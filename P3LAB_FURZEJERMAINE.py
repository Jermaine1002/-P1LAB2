# Jermaine Furze
# 2025-06-22
# P3LAB - Change Calculator
# This program accepts a float input for money and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies to make that amount.

'''
Pseudocode:
1. Ask the user to enter an amount of money (float with 2 decimals)
2. Multiply the amount by 100 and convert it to an integer (to get total cents)
3. Calculate the number of dollars using //
4. Subtract the dollar amount from the total cents
5. Repeat the same process for quarters, dimes, nickels, and pennies
6. Only display coins that are used (skip zero values)
7. Use singular/plural appropriately when displaying coin names
'''

# Get user input
amount = float(input("Enter amount in dollars and cents (e.g., 1.41): "))

# Convert to cents to avoid floating-point issues
cents = int(round(amount * 100))

# Dictionary to store coin values and names
coin_values = {
    "Dollar": 100,
    "Quarter": 25,
    "Dime": 10,
    "Nickel": 5,
    "Penny": 1
}

# Empty list to store output lines
output_lines = []

# Calculate each coin count
for coin_name, coin_value in coin_values.items():
    count = cents // coin_value
    cents = cents % coin_value
    if count == 1:
        output_lines.append(f"{count} {coin_name}")
    elif count > 1:
        # Pluralize coin name by adding 's'
        plural_name = "Pennies" if coin_name == "Penny" else coin_name + "s"
        output_lines.append(f"{count} {plural_name}")

# Output results
for line in output_lines:
    print(line)
