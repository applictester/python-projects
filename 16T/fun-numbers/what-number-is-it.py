def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    # A perfect number is a number that is equal to the sum of its proper divisors
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i  # Add the divisor to the sum
    return divisor_sum == n  # Check if the sum of divisors equals the number


def is_armstrong(n):
    # An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits
    # Initialize a variable to store the sum of powers
    total = 0
    # Calculate the number of digits without converting to a string
    num_digits = 0
    temp = n
    while temp > 0:
        temp //= 10
        num_digits += 1
    # Initialize a temporary variable to process the number
    temp = n
    # Loop through each digit
    while temp > 0:
        # Extract the last digit
        digit = temp % 10
        # Raise it to the power of num_digits and add to total
        total += digit**num_digits
        # Remove the last digit
        temp //= 10
    # Check if the sum of powers equals the original number
    return total == n


def is_automorphic(n):
    # An automorphic number is a number whose square ends with the same digits as the number itself
    square = n**2
    temp = n
    while temp > 0:
        if temp % 10 != square % 10:
            return False
        temp //= 10
        square //= 10
    return True


def is_lyndon(n):
    # Check if the number has an even number of digits
    temp = n
    num_digits = 0
    while temp > 0:
        temp //= 10
        num_digits += 1
    if num_digits % 2 != 0:
        return False
    # Split the number into two halves without using strings
    temp = n
    digits = []
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()
    mid = len(digits) // 2
    first_half = 0
    second_half = 0
    for i in range(mid):
        first_half = first_half * 10 + digits[i]
    for i in range(mid, len(digits)):
        second_half = second_half * 10 + digits[i]
    # Check if the sum of squares of the halves equals the number
    return first_half**2 + second_half**2 == n

def is_happy(n):
    # Convert the number to a list of digits
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()

    # Check if the number has an even number of digits
    if len(digits) % 2 != 0:
        return False

    # Split the digits into two halves
    mid = len(digits) // 2
    first_half = digits[:mid]
    second_half = digits[mid:]

    # Calculate the sum of each half
    return sum(first_half) == sum(second_half)
    

def is_symmetric(n):
    # A symmetric number is a number that reads the same forwards and backwards
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num

try:
    number = int(input("Введіть число: "))
    print(f"Число {number} є Простим: {is_prime(number)}")
    print(f"Число {number} є Досконалим: {is_perfect(number)}")
    print(f"Число {number} є Армстронга: {is_armstrong(number)}")
    print(f"Число {number} є Автоморфним: {is_automorphic(number)}")
    print(f"Число {number} є Ліндона: {is_lyndon(number)}")
    print(f"Число {number} є Щасливим: {is_happy(number)}")
    print(f"Число {number} є Симетричним: {is_symmetric(number)}")
except ValueError:
    print("Будь ласка, введіть коректне ціле число.")
