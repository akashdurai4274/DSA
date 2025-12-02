import math

def find_prime(n):
    if n < 2:
        return False
    divisors = []
    half = int(math.sqrt(n)) + 1
    for i in range(1, half):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors) == 2


# Algorithm - Sieve of Eratosthenes(more optimal)
def find_prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes[n]

print(find_prime(0))
print(find_prime(3))
print(find_prime(5))
print(find_prime(4))
print(find_prime(97))
print(find_prime_sieve(98))

primes = [n for n in range(2, 105) if find_prime_sieve(n)]
print(primes)