def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


try:
    n = int(input("Enter a number (n): "))
    print(f"Prime numbers from 0 to {n}:")
    for i in range(n + 1):
        if is_prime(i):
            print(i, end=" ")
except ValueError:
    print("Please enter a valid integer.")
