"""
Compute the Nth lexicographic permutation of the digits 0, 1, 2, ..., 9.

Approach: 
We use a bit of math compute this in constant time. Specifically, we know that the 
number of permutations of n digits is n!, so the (n+1)th digit increments every n! 
permutations. We express N as a_0 * 0! + a_2 * 1! + ... + a_9 * 9! (think of this 
as "base-factorial"). We then construct the Nth permutation by using these coefficients 
(a_0, ... a_9) as the amount to increment each digit by.
"""

N = 1000000
DIGITS = 9  # permute digits 0-9

def lexicographic_permutations(order):
    factorials = [1]
    for d in range(1, DIGITS + 1):
        factorials.append(d * factorials[d - 1])

    # Express N as a_0 * 0! + a_2 * 1! + ... + a_D * D! where D := DIGITS
    coefficients = [0 for _ in range(len(factorials))]
    remainder = order
    for d in range(len(factorials) - 1, -1, -1):
        coefficients[d] = remainder // factorials[d]
        remainder %= factorials[d]
    coefficients = list(reversed(coefficients))
    
    # Construct the Nth permutation
    result = [None for _ in range(DIGITS + 1)]
    for i in range(len(coefficients)):
        next_digits = sorted(list(set(range(len(coefficients))) - set(result)))
        result[i] = next_digits[coefficients[i]]
    return "".join([str(r) for r in result])

if __name__ == "__main__":
    print(f"Result = {lexicographic_permutations(N - 1)}")