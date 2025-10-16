import random

n = int(input("Введіть кількість елементів у списку: "))

# Генеруємо список з унікальних чисел від 0 до n-1 (всього n елементів)
numbers = list(range(0, n - 1))
# Перемішуємо список
random.shuffle(numbers)

print("Початковий список:", numbers)

# Знаходимо індекси мінімального та максимального елементів
min_index = 0
max_index = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    if numbers[i] > numbers[max_index]:
        max_index = i

# Міняємо місцями мінімальний та максимальний елемент
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список після заміни мінімального та максимального елементів:", numbers)