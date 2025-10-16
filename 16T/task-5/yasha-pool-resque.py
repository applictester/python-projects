# Введення даних
N = int(input("Введіть довжину басейну (N): "))
if N <= 0 :
    print("Помилка: некоректні розміри басейну.")
    exit()
M = int(input("Введіть ширину басейну (M < N): "))
if M <= 0 or M > N:
    print("Помилка: некоректні розміри басейну.")
    exit()

x = int(input("Введіть відстань до короткого бортика (x < N): "))
if x <= 0 or x > N:
    print("Помилка: координати виходять за межі басейну.")
    exit()

y = int(input("Введіть відстань до довгого бортика (y < M): "))
if y <= 0 or y > M:
    print("Помилка: координати виходять за межі басейну.")
    exit()

# Обчислення мінімальної відстані до борту
if x < N - x:
    min_distance_x = x
else:
    min_distance_x = N - x

if y < M - y:
    min_distance_y = y
else:
    min_distance_y = M - y

# Мінімальна відстань до борту
if min_distance_x < min_distance_y:
    min_distance = min_distance_x
else:
    min_distance = min_distance_y

# Виведення результату
print(f"Мінімальна відстань, яку потрібно проплисти Яші: {min_distance} метрів")
print(f"Перевірка: {min_distance==min(min_distance_x, min_distance_y)}")
