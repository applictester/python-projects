import random

n = int(input("Введіть кількість елементів у списку: "))
lst = [random.randint(0, 9) for _ in range(n)]
print("Список:", lst)

# Пошук унікальних елементів без використання словників
unique_elements = []
for i in range(len(lst)):
    is_unique = True
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            is_unique = False
            break
    if is_unique:
        unique_elements.append(lst[i])

print("Елементи, які зустрічаються лише один раз:", unique_elements)