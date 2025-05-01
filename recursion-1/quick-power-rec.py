def quick_power(a, n):
    """
    Function to calculate a^n using the fast exponentiation algorithm.
    Time complexity: O(log(n))
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = quick_power(a, n / 2)
        return half_power * half_power
    else:
        return a * quick_power(a, n - 1)

# Example usage
a = 2
n = 10
result = quick_power(a, n)
print(f"{a}^{n} = {result}")