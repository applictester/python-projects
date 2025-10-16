# Введення кількості чисел
n = int(input("Введіть кількість чисел: "))

# Ініціалізація змінної для збереження максимального числа
max_number = None

# Цикл для введення чисел і пошуку максимального
for i in range(n):
    num = float(input(f"Введіть число {i + 1}: "))
    if max_number is None or num > max_number:
        max_number = num

# Виведення максимального числа
if max_number.is_integer():
    print("Максимальне число:", int(max_number))
else:
    print("Максимальне число:", max_number)