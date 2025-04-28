def season(month):
    if month in (12, 1, 2):
        return "зима"
    elif month in (3, 4, 5):
        return "весна"
    elif month in (6, 7, 8):
        return "літо"
    elif month in (9, 10, 11):
        return "осінь"
    else:
        return "Невірний номер місяця"

# Приклад використання
month = int(input("Введіть номер місяця (1-12): "))
print("Пора року:", season(month))