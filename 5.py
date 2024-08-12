'''
Computes the smallest positive number that is evenly divisible by all the numbers from 1 to N.

Approach: We want to take the product of all the numbers n from 1 to N, omitting 
repeated factors. We can remove repeated factors by going through each n and dividing it
out from its successors. Then the answer is the product of the final list.
'''
from functools import reduce

N = 20

def smallest_divisible():
    factors = list(range(2, N+1))
    for i, d in enumerate(factors):
        for j in range(i+1, len(factors)):
            if factors[j] % d == 0:
                factors[j] //= d
    result = reduce(lambda x, y: x * y, factors)
    print(f"{factors=}")
    print(f"{result=}")
    return result
    
if __name__ == "__main__":
    smallest_divisible()