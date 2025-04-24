def is_armstrong_number(num):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d**power for d in digits)


def print_armstrong_numbers_to_n(n):
    """Print all Armstrong numbers up to n."""
    for i in range(n + 1):
        if is_armstrong_number(i):
            print(i)


try:
    n = int(input("Enter a number (n): "))
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        print(f"Armstrong numbers up to {n}:")
        print_armstrong_numbers_to_n(n)
except ValueError:
    print("Invalid input. Please enter an integer.")  # test comment
