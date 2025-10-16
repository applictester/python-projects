# Введення кількості чисел
n = int(input("Введіть кількість чисел: "))

# Ініціалізація змінних для мінімального та максимального значень
min_value = float('inf')
max_value = float('-inf')

# Цикл для введення чисел та знаходження мінімального і максимального
for i in range(n):
    num = float(input(f"Введіть число {i + 1}: "))
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

# Обчислення середнього арифметичного мінімального та максимального
average = (min_value + max_value) / 2

# Виведення результату
print(f"Мінімальне число: {int(min_value) if min_value.is_integer() else min_value}")
print(f"Максимальне число: {int(max_value) if max_value.is_integer() else max_value}")
print(f"Середнє арифметичне мінімального та максимального: {int(average) if average.is_integer() else average}")