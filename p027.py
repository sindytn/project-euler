"""
Compute the product a * b such that n^2 + a * n + b is prime for the longest sequence of
consecutive n starting with n = 0.

Approach:
Brute force. Iterate through all possible combinations of |a| < 1000, |b| < 1000, 
evaluate the result of the quadratic equation, and check if it's prime. Keep track of 
the longest sequence (n) so far and the coefficients (a, b) that produce it. 
"""

import math

MAX_A = 999
MAX_B = 999

def is_prime(n):
    if n < 2:
        return False
    for m in range(2, int(math.sqrt(n)) + 1):
        if n % m == 0:
            return False
    return True

def quadratic_primes():
    optimal_a = None
    optimal_b = None
    max_n = None

    for a in range(-MAX_A, MAX_A + 1):
        for b in range(MAX_B + 1):
            # b must be prime to satisfy n^2 + a * n + b is prime when n = 0
            if not is_prime(b):
                continue
            n = 0
            has_seen_composite = False
            while not has_seen_composite:
                n += 1
                has_seen_composite = not is_prime(n ** 2 + a * n + b)
            if max_n is None or max_n < n - 1:
                max_n = n
                optimal_a = a
                optimal_b = b
            
    print(f"a = {optimal_a}, b = {optimal_b}")
    return optimal_a * optimal_b

if __name__ == "__main__":
    print(f"Result = {quadratic_primes()}")
