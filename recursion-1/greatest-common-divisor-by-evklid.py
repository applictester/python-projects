def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Приклад використання
a = 1071
b = 462
result = gcd(a, b)
print(f"НСД({a}, {b}) = {result}")