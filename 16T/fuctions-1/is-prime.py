def is_prime(number):
    if number < 2 or number > 1000:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number between 0 and 1000: "))
if num < 0 or num > 1000:
    print("Number out of range. Please enter a number between 0 and 1000.")
elif is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")