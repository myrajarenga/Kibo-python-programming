# Write your solution below
# Follow the instructions in the tab to the right

# Use this exchange rate
NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021

USD_value = float(input("Entre the amount of USD to convert to NGN: "))

value = USD_value * NAIRA_PER_DOLLAR

print(f"USD_value is {value:.2f} NGN")