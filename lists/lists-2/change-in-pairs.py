import random

n = int(input("Введіть кількість елементів: "))
A = [random.randint(1, 100) for _ in range(n)]
print("Початковий список:", A)

for i in range(0, n - 1, 2):
    A[i], A[i + 1] = A[i + 1], A[i]

print("Список після перестановки в парах:", A)