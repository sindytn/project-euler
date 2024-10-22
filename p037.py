"""
Find the primes that remain prime as you truncate digits left to right or right to left.

Approach: Brute force. 
"""
from p027 import is_prime

NUM_PRIMES = 11

def is_truncated_prime(x):
    x_str = str(x)
    for i in range(len(x_str)):
        if not is_prime(int(x_str[i:])) or not is_prime(int(x_str[:i+1])):
            return False
    return True

def truncatable_primes():
    primes = []
    x = 11                              # Start with 11 since 2, 3, 5, 7 don't count
    while len(primes) < NUM_PRIMES:
        if is_truncated_prime(x):
            primes.append(x)
        x += 1
    # print(primes)
    return sum(primes)

if __name__ == "__main__":
    print(f"Result = {truncatable_primes()}")