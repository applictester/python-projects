import random

# Введення кількості елементів
n = int(input("Введіть кількість елементів у списку: "))

# Генерація списку додатніх цілих чисел від 0 до 9
lst = [random.randint(0, 9) for _ in range(n)]

# Виведення списку
print("Список:", lst)

pairs = 0
i = 0
while i < len(lst):
    el = lst[i]
    # Шукаємо ще один такий самий елемент
    found = False
    for j in range(i+1, len(lst)):
        if lst[j] == el:
            # Видаляємо обидва елементи зі списку
            lst.pop(j)
            lst.pop(i)
            pairs += 1
            found = True
            break
    if not found:
        i += 1

print("Кількість пар з однакових елементів:", pairs)