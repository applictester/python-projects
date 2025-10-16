def bank(a, years):
    while years > 0:
        a += a * 0.10  # Add 10% interest to the deposit
        years -= 1
    return round(a, 2)  # Return the result rounded to 2 decimal places


def bank2(a, years):
    for _ in range(years):
        a += a * 0.10  # Add 10% interest to the deposit
    return round(a, 2)  # Return the result rounded to 2 decimal places


# Example usage
initial_deposit = float(input("Enter the initial deposit amount (in UAH): "))
deposit_years = int(input("Enter the number of years: "))
final_amount = bank(initial_deposit, deposit_years)
print(f"The total amount after {deposit_years} years will be: {final_amount} UAH")
print(f"Checking with bank2: {bank2(initial_deposit, deposit_years)} UAH")
