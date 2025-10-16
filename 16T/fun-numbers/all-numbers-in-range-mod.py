def get_divisors(n):
    # Find all divisors of the number
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors  


def count_digits(n):
    # Calculate the number of digits without converting to a string
    num_digits = 0
    while n > 0:
        n //= 10
        num_digits += 1
    return num_digits


def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits


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
    divisors = get_divisors(n)
    return sum(divisors) == n  # Check if the sum of divisors equals the number


def is_armstrong(n):
    # An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits
    # Initialize a variable to store the sum of powers
    total = 0
    num_digits = count_digits(n)
    # Initialize a temporary variable to process the number
    temp = n
    # Loop through each digit
    while temp > 0:
        # Extract the last digit
        digit = temp % 10
        # Raise it to the power of num_digits and add to total
        total += digit ** num_digits
        # Remove the last digit
        temp //= 10
    # Check if the sum of powers equals the original number
    return total == n

def is_automorphic(n):
    # An automorphic number is a number whose square ends with the same digits as the number itself
    square = n ** 2
    temp = n
    while temp > 0:
        if temp % 10 != square % 10:
            return False
        temp //= 10
        square //= 10
    return True


def is_lyndon(n):
    # Check if the number has an even number of digits
    if count_digits(n) % 2 != 0:
        return False
    # Split the number into two halves without using strings
    digits = get_digits(n)
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
    digits = get_digits(n)

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
    start = int(input("Введіть початок інтервалу: "))
    end = int(input("Введіть кінець інтервалу: "))

    # наглядна форма формування списків
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    # скорочена форма формування списків
    perfects = [n for n in range(start, end + 1) if is_perfect(n)]
    armstrongs = [n for n in range(start, end + 1) if is_armstrong(n)]
    automorphics = [n for n in range(start, end + 1) if is_automorphic(n)]
    lyndons = [n for n in range(start, end + 1) if is_lyndon(n)]
    happies = [n for n in range(start, end + 1) if is_happy(n)]
    symmetrics = [n for n in range(start, end + 1) if is_symmetric(n)]

    print(f"Прості числа: {primes}")
    print(f"Досконалі числа: {perfects}")
    print(f"Числа Армстронга: {armstrongs}")
    print(f"Автоморфні числа: {automorphics}")
    print(f"Числа Ліндона: {lyndons}")
    print(f"Щасливі числа: {happies}")
    print(f"Симетричні числа: {symmetrics}")
except ValueError:
    print("Будь ласка, введіть коректні цілі числа.")
