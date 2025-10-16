import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Зчитування чотирьох дійсних чисел
x1 = float(input("Введіть x1: "))
y1 = float(input("Введіть y1: "))
x2 = float(input("Введіть x2: "))
y2 = float(input("Введіть y2: "))

# Обчислення та виведення результату
result = distance(x1, y1, x2, y2)
print(f"Відстань між точками: {result}")