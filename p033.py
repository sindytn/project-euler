"""
Find the non-trivial fractions a / b for two-digit a and b where cancelling the common 
digit from the numerator and denominator evaluates correctly.

Approach:
Brute force. Iterate through all possible combinations of a and b, remove the common 
digit if any, then check for correctness.
"""
from p021 import compute_proper_divisors
from functools import reduce

def simplify_fraction(a, b):
    if b % a == 0:
        return (1, b // a)
    greatest_common_divisor = max(compute_proper_divisors(a).intersection(compute_proper_divisors(b)))
    return (a // greatest_common_divisor, b // greatest_common_divisor)


def digit_cancelling_fractions():
    fractions = []
    for a in range(10, 100):
        for b in range(a + 1, 100):
            digits_a = [int(x) for x in list(str(a))]
            digits_b = [int(x) for x in list(str(b))]
            common_digits = set(digits_a).intersection(set(digits_b))
            if len(common_digits) < 1:
                continue
            # Omit trivial fractions like 30/50 = 3/5
            if a % 10 == 0 and b % 10 == 0:
                continue
            for common_digit in common_digits:
                a_trunc = digits_a.copy()
                b_trunc = digits_b.copy()
                a_trunc.remove(common_digit)
                b_trunc.remove(common_digit)
                # Don't divide by zero
                if b_trunc[0] == 0:
                    continue
                if a_trunc[0] / b_trunc[0] == a / b:
                    fractions.append((a, b))
    # print(f"{fractions=}")
    product = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), fractions)
    denominator = simplify_fraction(*product)[1]
    return denominator

if __name__ == "__main__":
    print(f"Result = {digit_cancelling_fractions()}")