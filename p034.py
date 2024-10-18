"""
Find the numbers equal to the sum of the factorial of their digits. Return the sum.

Approach:
We start by identifying an upper limit. For each number x, adding a digit 
increases it by an order of 10. The sum of the factorial of digits is at most 
9! * (number of digits). The former grows faster than the latter, so after some trial 
and error, we notice that the max x can have no more than 7 digits.

We use this maximum as the stopping condition for a brute force iteration.
"""
from functools import reduce

def factorial(x):
    if x in [0, 1]:
        return 1
    return reduce(lambda a, b: a * b, list(range(1, x + 1)))
    
def digit_factorials():
    max_x = factorial(9) * 7        # 9999999 > (7 * 9! = 2540160)
    numbers = []
    for x in range(3, max_x):
        digits = [int(digit) for digit in list(str(x))]
        if x == sum([factorial(d) for d in digits]):
            numbers.append(x)
    return sum(numbers)

if __name__ == "__main__":
    print(f"Result = {digit_factorials()}")