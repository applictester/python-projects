# Програма для перевірки, чи може шаховий ферзь потрапити з однієї клітини на іншу одним ходом

# Введення координат першої та другої клітини
x1 = int(input("Введіть номер стовпця першої клітини (1-8): "))
y1 = int(input("Введіть номер рядка першої клітини (1-8): "))
x2 = int(input("Введіть номер стовпця другої клітини (1-8): "))
y2 = int(input("Введіть номер рядка другої клітини (1-8): "))

# Перевірка, чи може ферзь потрапити з першої клітини на другу
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("Ферзь може потрапити з першої клітини на другу одним ходом.")
else:
    print("Ферзь не може потрапити з першої клітини на другу одним ходом.")