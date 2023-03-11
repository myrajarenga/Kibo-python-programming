usd_value = float(input("Enter the amount of USD to convert to NGN: "))

NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021

ngn_value = usd_value * NAIRA_PER_DOLLAR

print(f"{usd_value:.2f} USD is {ngn_value:.2f} NGN")