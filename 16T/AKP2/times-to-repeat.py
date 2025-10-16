# https://basecamp.eolymp.com/uk/problems/20

def sum_of_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def times_to_repeat(n):
    count = 0
    while n > 0:
        n -= sum_of_digits(n)
        count += 1
    return count


n = int(input())
print(times_to_repeat(n))
