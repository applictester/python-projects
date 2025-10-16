# Програма для знаходження найменшого з трьох цілих чисел за допомогою if-else

# Введення трьох цілих чисел
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

# Знаходження найменшого числа
if a <= b and a <= c:
    min_number = a
elif b <= a and b <= c:
    min_number = b
else:
    min_number = c

# Виведення результату
print("Найменше число:", min_number)
print("Перевірка:", min(a, b, c)==min_number)