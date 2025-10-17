# https://uk.wikipedia.org/wiki/Решето_Ератосфена
# https://eolymp.com/uk/problems/1302

def sieve(n):
    limit = int(n**0.5) + 1
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return is_prime


def almost_primes(m, n, is_prime):
    """Return list of almost-prime numbers in [m, n] using sieve array is_prime[]."""
    if m > n:
        return []
    res = []
    limit = int(n**0.5) + 1
    for p in range(2, limit):
        if not is_prime[p]:
            continue
        power = p * p
        while power <= n:
            if power >= m:
                res.append(power)
            power *= p
    res.sort()  # optional: ensures ascending order
    return res


def count_almost_primes(m, n, is_prime):
    """Return how many almost-prime numbers are in [m, n]."""
    if m > n:
        return 0
    count = 0
    limit = int(n**0.5) + 1
    for p in range(2, limit):
        if not is_prime[p]:
            continue
        power = p * p
        while power <= n:
            if power >= m:
                count += 1
            power *= p
    return count


k = int(input())
matrix = []
for _ in range(k):
    matrix.append(list(map(int, input().split())))

for row in matrix:
    # print(row)
    m, n = row
    is_prime = sieve(n)
    # print(almost_primes(m, n, is_prime))
    print(count_almost_primes(m, n, is_prime))
