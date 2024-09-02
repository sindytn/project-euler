"""
Computes the sum of amicable numbers less than N.

Approach:
Brute force. We compute and store the sum of proper divisors of every number up to N. 
Then check each number for amicable-ness by looking up in the stored table.
"""

N = 10000

def compute_proper_divisors(num):
    result = [1]
    for n in range(2, int(num ** (1/2))):
        if num % n == 0:
            result += [n, num // n]
    return result

def amicable_numbers_sum():
    proper_divisors = {}
    for n in range (2, N):
        proper_divisors[n] = compute_proper_divisors(n)
    proper_divisor_sums = {n: sum(proper_divisors[n]) for n in proper_divisors}
    amicable_numbers = set([])
    for a, b in proper_divisor_sums.items():
        if a != b and b in proper_divisor_sums and proper_divisor_sums[b] == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return sum(amicable_numbers)

if __name__ == "__main__":
    print(f"Result = {amicable_numbers_sum()}")
