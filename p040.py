"""
Find the digits in the [1, 10, 100, ..., 10e6] places of the number formed by 
concatenating the natural numbers 1, 2, 3, ...

Approach:
Iterate through all the natural numbers until we find the 10e6-th digit. O(n) time, O(1)
space, where n is 10e6. We achieve O(1) space by storing only the index of the last seen
digit instead of all the seen digits.
"""

from functools import reduce

INDICES = [10 ** i for i in range(7)]

def champernowne_constant():
    digits = []
    num_seen_digits = 0

    for i in range(1, int(10e6)):
        if len(INDICES) <= len(digits):
            break
        next_index = INDICES[len(digits)]
        new_digits = [int(d) for d in str(i)]
        if next_index <= num_seen_digits + len(new_digits):
            index_into_new_digits = next_index - num_seen_digits
            digits.append(new_digits[index_into_new_digits - 1])
        num_seen_digits += len(new_digits)

    return reduce(lambda x, y: x * y, digits)  # product

if __name__ == "__main__":
    print(f"Result = {champernowne_constant()}")