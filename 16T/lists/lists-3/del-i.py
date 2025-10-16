import random

lst = []
while len(lst) < 10:
    num = random.randint(1, 99)
    if num not in lst:
        lst.append(num)
print("Початковий список:", lst)

k = int(input(f"Введіть індекс елемента, який потрібно видалити (0 до {len(lst) - 1}): "))

for i in range(k, len(lst) - 1):
    lst[i] = lst[i + 1]

lst.pop()  # By default, the pop() method uses an index of -1, which refers to the last item in the list.

print("Список після видалення елемента:", lst)
