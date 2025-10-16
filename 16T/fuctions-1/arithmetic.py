def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Ділення на нуль неможливе"
    else:
        return "Невідома операція"

# Приклад використання
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
op = input("Введіть операцію (+, -, *, /): ")

result = arithmetic(x, y, op)
print("Результат:", result)