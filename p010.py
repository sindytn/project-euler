"""
Computes the sum of primes less than N.

Approach 1 (slow): Build a list of primes iteratively. Start with 2, then check every 
new candidate against the seen primes. Take the sum at the end. We can add some tricks 
to speed it up slightly but O(n^2) is still too slow since N is 2e6.

Approach 2 (faster): Sieve of Eratosthenes. Start with the list of N possible candidates, 
then iteratively prune all the multiples of the current prime. The next prime is the 
next non-zero candidate. O(n log log n).
"""

import math

N = int(2e6)

def sum_of_primes_fast():
    primes = [0, 0] + list(range(2, N))
    for i in range(2, N // 2):
        if primes[i] != 0:
            for multiplier in range(2, math.ceil(N / primes[i])):
                primes[i * multiplier] = 0
    return sum(primes)

def sum_of_primes_slow():
    primes = [2]
    for n in range(3, N, 2):
        is_prime = True
        for p in primes:
            if p > n / 2:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return sum(primes)

if __name__ == "__main__":
    print(f"Result = {sum_of_primes_fast()}")