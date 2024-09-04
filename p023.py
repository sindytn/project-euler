"""
Computes the sum of all positive integers that can't be expressed as the sum of two 
abundant numbers.

Approach: 
Compute all abundant nums. Use the same method as in problem 21 to get proper divisors 
for each number. Compute all the numbers under the given limit (28123) which *can* be
expressed as the sum of abundant numbers, then find the complement of this set.
"""

from p021 import compute_proper_divisors

N = 28123

def non_abundant_sum():
    # Get all abundant nums <N
    abundant_nums = []
    for n in range(1, N + 1):
        if sum(compute_proper_divisors(n)) > n:
            abundant_nums.append(n)

    # Track all abundant sums
    abundant_sums = []
    for n in range(len(abundant_nums)):
        for m in range(n, len(abundant_nums)):
            a = abundant_nums[n]
            b = abundant_nums[m]
            abundant_sums.append(a + b)
    return sum(set(range(N)) - set(abundant_sums))

if __name__ == "__main__":
    print(f"Result = {non_abundant_sum()}")