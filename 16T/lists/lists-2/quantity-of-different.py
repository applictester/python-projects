import random

def count_unique_elements(lst):
    count = 1 if lst else 0  # if lst перевіряє, чи список lst містить хоча б один елемент
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            count += 1
    print("Кількість різних елементів:", count)


n = int(input("Введіть кількість елементів: "))
numbers = [random.randint(0, 10) for _ in range(n)]

# Сортуємо список
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Відсортований список:", numbers)
# Викликаємо функцію
count_unique_elements(numbers)
