"""
Computes the smallest triangle number to have at least N divisors.

Approach: 
First, simplify the problem with some math facts:
1) 1 + 2 + ... + n = n * (n + 1) / 2
2) n and (n + 1) have no shared divisors
3) Consider the prime factorization of a given number n: n = p1^k1 + p2^k2 + ... pm^km. 
   The number of divisors of n is (k1 + 1) * (k2 + 1) * ... * (km + 1)

Knowing these, we use the following algorithm:
1) Consider each n such that the triangle number is (n - 1) * n / 2, starting at n = 2. 
   Compute its prime factorization by looking for the smallest divisor, then reusing the
   previously seen prime factorization for its quotient.
2) Compute and store the number of divisors of n
3) Compute the number of divisors of the triangle number (n - 1) * n / 2 using the 
   number of divisors, each, of (n - 1) and n
"""

import math

MIN_DIVISORS = 500

def triangle_number_divsors():
    prime_factorizations = [{}, {}]     # nth value is the prime factorization of n, {p1: k1, p2: k2, ...} such that n = p1^k1 * p2^k2 * ...
    num_divisors = [0, 1]               # nth value is the number of divisors of n
    n = 2
    while True:
        # Get num divisors of n
        is_prime = True                 # is n prime
        prime_factorizations.append({})
        num_divisors.append(1)
        for m in range(2, int(math.sqrt(n)) + 1):
            if n % m == 0:
                q = n // m              # quotient
                prime_factorizations[n] = dict(prime_factorizations[q])
                prime_factorizations[n][m] = prime_factorizations[n][m] + 1 if m in prime_factorizations[n] else 1
                for x in prime_factorizations[n].values():
                    num_divisors[n] *= (x + 1) 
                is_prime = False
                break
        if is_prime:
            prime_factorizations[n] = {n: 1}
            num_divisors[n] = 2

        # Check num divisors in triangle number 1 + 2 + ... + (n - 1)
        triangle_num_divisors = num_divisors[n // 2] * num_divisors[n-1] if n % 2 == 0 else num_divisors[n] * num_divisors[(n - 1) // 2]
        if triangle_num_divisors > MIN_DIVISORS:
            return n * (n - 1) // 2
        n += 1

if __name__ == "__main__":
    print(f"Result = {triangle_number_divsors()}")