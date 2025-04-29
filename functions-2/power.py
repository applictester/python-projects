def power(a, n):
    result = 1
    for _ in range(abs(n)):
        result *= a
    if n < 0:
        return 1 / result
    return result

# Example usage:
a = float(input("Enter a positive number (a): "))
n = int(input("Enter an integer (n): "))
print(f"{a} raised to the power of {n} is: {power(a, n)}")