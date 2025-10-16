def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "YES"
    else:
        return "NO"

# Input a natural number
year = int(input("Enter a year: "))
print(is_leap_year(year))