def sign_of_x(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# Завдання «Знак числа»
x = float(input("Enter a number: "))
print(f"The sign of {x} is {sign_of_x(x)}")
