"""
Find all the primes less than 1e6 such that all rotations of each prime are also prime.

Approach:
First we notice that primes cannot end in an even digit or 5, since that would imply 
divisibility by 2 or 5, respectively. Therefore, circular primes cannot contain any of 
these digits; it must be exclusively made up of {1, 3, 7, 9}. We do a brute force 
iteration on all the possible combinations of this reduced set of digits.
"""
from p027 import is_prime

MAX = 1000000

def circular_primes():
    primes = [2, 3, 5, 7]
    for x in range(11, MAX):
        digits = [int(digit) for digit in list(str(x))]
        if any([d in [0, 2, 4, 5, 6, 8] for d in digits]):
            continue
        rotations = []
        for i in range(len(digits)):
            rotations.append(int(''.join([str(d) for d in digits[i:] + digits[:i]])))
        if all([is_prime(r) for r in rotations]):
            primes.extend(rotations)
    # print(sorted(list(set(primes))))
    return len(set(primes))

if __name__ == "__main__":
    print(f"Result = {circular_primes()}")