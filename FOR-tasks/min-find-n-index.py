# Введення кількості чисел
n = int(input("Введіть кількість чисел: "))

# Ініціалізація змінних
min_value = None
min_index = -1

# Введення чисел та пошук мінімального
for i in range(n):
    num = float(input(f"Введіть число {i + 1}: "))
    if min_value is None or num < min_value:
        min_value = num
        min_index = i + 1  # Зберігаємо порядковий номер (починаючи з 1)

# Виведення результату
if min_value.is_integer():
    print(f"Мінімальне число: {int(min_value)}")
else:
    print(f"Мінімальне число: {min_value}")
print(f"Його порядковий номер: {min_index}")