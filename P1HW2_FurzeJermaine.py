# Jermaine Furze
# 2025-06-22
# P1HW2 - Travel Budget Calculator
# This program asks the user to enter a budget and travel expenses,
# then it calculates the total expenses and the remaining balance for the trip.

'''
Pseudocode:
1. Ask the user to enter their budget
2. Ask the user to enter their travel destination
3. Ask the user to enter amount they will spend on gas
4. Ask the user to enter amount they will spend on accommodation
5. Ask the user to enter amount they will spend on food
6. Calculate total expenses (gas + accommodation + food)
7. Subtract total expenses from budget to get remaining balance
8. Display destination, budget, individual expenses, total expenses, and remaining balance
'''

# Input section
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculations
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Output section
print("\n------------Travel Expenses------------")
print(f"Location:              {destination}")
print(f"Initial Budget:        ${budget}")
print(f"Fuel:                  ${gas}")
print(f"Accommodation:         ${accommodation}")
print(f"Food:                  ${food}")
print("---------------------------------------")
print(f"Remaining Balance:     ${remaining_balance}")
