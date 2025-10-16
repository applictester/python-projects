def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

# Example usage
a = float(input("Enter a positive real number (a): "))
n = int(input("Enter a non-negative integer (n): "))

if a > 0 and n >= 0:
    print(f"{a} raised to the power of {n} is {power(a, n)}")
else:
    print("Invalid input. 'a' must be positive and 'n' must be non-negative.")