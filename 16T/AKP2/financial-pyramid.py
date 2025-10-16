# https://basecamp.eolymp.com/uk/problems/140

n = int(input())

debt = 2  # борг після 1-го дня
eat = 2  # з’їв на 1-й день
borrowed = 2  # скільки позичив на 1-й день

if n == 1:
    print(eat, debt)
else:
    for day in range(2, n + 1):
        borrowed *= 2 # позичив вдвічі більше ніж борг на початок дня
        pay = (debt + borrowed) // 2 # сплатив половину боргу, враховуючи позичене в цей день
        eat = borrowed - pay # з’їв різницю між позиченим та сплаченим
        debt = debt - pay + borrowed # борг на кінець дня зменшився на сплачену частину, але збільшився на позичене

    print(eat, debt)
