def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example usage
year = int(input("Enter a year: "))
if is_year_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")