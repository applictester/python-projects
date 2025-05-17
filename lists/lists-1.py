import random

# Генеруємо масив з 50 цілих чисел різних знаків
arr = [random.randint(-100, 100) for _ in range(50)]


print("Масив:")
print(arr)

# 1. Парні індекси
def even_indices(lst):
    print("Елементи з парними індексами:")
    for i in range(0, len(lst), 2):
        print(lst[i])

# 2. Парні елементи
def even_elements(lst):
    print("Парні елементи:")
    # Створюємо новий список тільки з парних елементів
    even_list = []
    for x in lst:
        if x % 2 == 0:
            even_list.append(x)
    print(even_list)

# 3. Більше попереднього
def greater_than_previous(lst):
    # Створимо новий список, у який додамо лише ті елементи,
    # які більші за попередній елемент у списку
    result = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            result.append(lst[i])
    print("Елементи, більші за попередній:")
    print(result)


# 4. Сусіди одного знаку
def same_sign_neighbors(lst):
    for i in range(len(lst)-1):
        if lst[i] * lst[i+1] > 0:
            print("Пара сусідів одного знаку:", lst[i], lst[i+1])
            return
    # Якщо не знайдено, нічого не виводимо

# 5. Більше за своїх сусідів
def greater_than_neighbors(lst):
    count = 0
    for i in range(1, len(lst)-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            count += 1
    print("Кількість елементів, більших за своїх сусідів:", count)

# 6. Найбільший елемент
def max_element(lst):
    max_val = lst[0]
    idx = 0
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            idx = i
    print("Найбільший елемент:", max_val)
    print("Індекс першого найбільшого елемента:", idx)

# Демонстрація роботи функцій
even_indices(arr)
even_elements(arr)
greater_than_previous(arr)
same_sign_neighbors(arr)
greater_than_neighbors(arr)
max_element(arr)
