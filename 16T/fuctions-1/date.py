def is_leap_year(year):
    """Перевіряє, чи є рік високосним."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def date(day, month, year):
    """Перевіряє, чи є дата дійсною."""
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    # Кількість днів у кожному місяці
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Якщо рік високосний, лютий має 29 днів
    if is_leap_year(year):
        days_in_month[1] = 29

    # Перевірка, чи день не перевищує кількість днів у місяці
    return day <= days_in_month[month - 1]

# Приклад використання
day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік: "))

print(date(day, month, year))