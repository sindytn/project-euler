"""
Find the sum of all numbers c which can be expressed as a product a * b = c such that 
a, b, c use all the digits 1-9 exactly once.

Approach:
We start by finding ranges for a, b, and c and notice that they must 2, 3, 4 or 1, 4, 4 
digits respectively. Then we iterate through all the combinations of digits for a and b,
of which there are 9 * 8 * 7 * 6 * 5 = 15120. We track the remaining digits and check 
the product a * b against them.
"""

def pandigital_products():
    digits = list(range(1, 10))
    products = []
    for d1 in digits:
        d2_digits = digits.copy()
        d2_digits.remove(d1)
        for d2 in d2_digits:
            d3_digits = d2_digits.copy()
            d3_digits.remove(d2)
            for d3 in d3_digits:
                d4_digits = d3_digits.copy()
                d4_digits.remove(d3)
                for d4 in d4_digits:
                    d5_digits = d4_digits.copy()
                    d5_digits.remove(d4)
                    for d5 in d5_digits:
                        remaining_digits = d5_digits.copy()
                        remaining_digits.remove(d5)
                        # 2 digit * 3 digit = 4 digit
                        a = 10 * d1 + d2
                        b = 100 * d3 + 10 * d4 + d5
                        prod = a * b
                        prod_digits = [int(x) for x in list(str(prod))]
                        if len(prod_digits) == len(remaining_digits) and set(prod_digits) == set(remaining_digits):
                            products.append((a, b, prod))

                        # 1 digit * 4 digit = 4 digit
                        a = d1
                        b = 1000 * d2 + 100 * d3 + 10 * d4 + d5
                        prod = a * b
                        prod_digits = [int(x) for x in list(str(prod))]
                        if len(prod_digits) == len(remaining_digits) and set(prod_digits) == set(remaining_digits):
                            products.append((a, b, prod))
    return sum(set([prod[2] for prod in products]))

if __name__ == "__main__":
    print(f"Result = {pandigital_products()}")