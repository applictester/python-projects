# https://uk.wikipedia.org/wiki/Решето_Ератосфена
# https://eolymp.com/uk/problems/1302

import math
import bisect

# Almost Prime Numbers

almost_max = int(1e12)
primes_max = int(1e6)

# Sieve of Eratosthenes
primes = [True] * (primes_max + 1)
primes[0] = primes[1] = False
for i in range(2, int(math.isqrt(primes_max)) + 1):
    if primes[i]:
        for j in range(i * i, primes_max + 1, i):
            primes[j] = False

# Generate almost primes
almost = []
for i in range(2, primes_max + 1):
    if primes[i]:
        temp = i
        while temp * i <= almost_max:
            temp *= i
            almost.append(temp)

# Sort for binary search
almost.sort()

# Read input
k = int(input())
for _ in range(k):
    m, n = map(int, input().split())
    # Use bisect (binary search)
    count = bisect.bisect_right(almost, n) - bisect.bisect_right(almost, m - 1)
    print(count)
