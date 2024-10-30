"""
Find the largest pandigital prime.

Approach:
We notice that all pandigital numbers with 8 or 9 digits are divisible by 9. 
Omitting these reduces the set of numbers we need to check from 10^9 to 10^7. From 
there, we iterate in descending order and return the first pandigital prime.
"""
from p027 import is_prime

MAX_NUM_DIGITS = 9

def pandigital_prime():
    for num_digits in range(MAX_NUM_DIGITS, 0, -1):
        # Skip 8-digit and 9-digit pandigital numbers, which are divisible by 9
        if num_digits == 8 or num_digits == 9:
            continue

        digit_pool = set([str(d) for d in range(1, num_digits + 1)])
        max_x = int("".join([str(d) for d in range(num_digits, 0, -1)]))
        min_x = int("".join([str(d) for d in range(1, num_digits + 1)]))

        for x in range(max_x, min_x - 1, -1):
            if set(str(x)) != digit_pool:
                continue
            if is_prime(x):
                return x
    return 

if __name__ == "__main__":
    print(f"Result = {pandigital_prime()}")