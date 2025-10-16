# https://uk.wikipedia.org/wiki/Решето_Ератосфена

m, n = map(int, input().split())

def sieve_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

is_prime = sieve_eratosthenes(n)
primes = [i for i in range(m, n+1) if is_prime[i]]

if primes:
    for p in primes:
        print(p)
else:
    print("Absent")
