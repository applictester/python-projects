# Введення координат першої і другої клітин
x1 = int(input("Введіть номер стовпця першої клітини (1-8): "))
y1 = int(input("Введіть номер рядка першої клітини (1-8): "))
x2 = int(input("Введіть номер стовпця другої клітини (1-8): "))
y2 = int(input("Введіть номер рядка другої клітини (1-8): "))

# Перевірка, чи може слон потрапити з першої клітини на другу одним ходом
if abs(x1 - x2) == abs(y1 - y2):
    print("Слон може потрапити з першої клітини на другу одним ходом.")
else:
    print("Слон не може потрапити з першої клітини на другу одним ходом.")