"""
Computes the Nth prime.

Approach: Check each number against all the primes we have already seen. It is prime if 
none of the previously seen primes divide evenly into it.
"""
import math

N = 10001

def nth_prime():
    primes = []
    n = 2
    while (len(primes) < N):
        if not any([n % p == 0 for p in primes]):
            primes.append(n)
        n+= 1
    return primes[-1]

if __name__ == "__main__":
    print(f"Result = {nth_prime()}")