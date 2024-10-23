"""
Find the largest number containing each digit 1-9 exactly once that can be constructed 
as the concatenation of the product of some x with (1, 2, 3, ..., n) for n > 1.

Approach:
Since the problem gives us that 9 * (1,2,3,4,5) = 918273645, we can immediately reduce 
the pool of x to since it must begin with the digit 9. Then we iterate on this reduced 
pool to find all x that satisfy the condition and return the greatest product.
"""

def pandigital_multiples():
    pandigital_equations = []
    for x in range(10000):
        digits = [int(d) for d in str(x)]
        # Optimization: x must start with 9 since the first product is x * 1 and we know
        # that 9 * (1,2,3,4,5) = 918273645
        if digits[0] != 9:
            continue
        # Pandigital product includes digits 1-9 only
        if 0 in digits:
            continue
        # No repeats
        if len(set(digits)) != len(digits):
            continue

        concatenated_digits = []
        for i in range(1, 10):
            new_digits = [int(d) for d in str(x * i)]
            if len(set(new_digits)) != len(new_digits):
                break
            if 0 in new_digits:
                break
            if any([d in concatenated_digits for d in new_digits]):
                break
            concatenated_digits.extend(new_digits)
            if len(concatenated_digits) == 9:
                pandigital_equations.append((x, i, int(''.join([str(d) for d in concatenated_digits]))))
    # print(pandigital_equations)
    return max([eq[2] for eq in pandigital_equations])

if __name__ == "__main__":
    print(f"Result = {pandigital_multiples()}")