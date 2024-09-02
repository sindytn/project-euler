'''
Computes the difference between the sum of the squares of the first N numbers and the square of the sum.
'''
from functools import reduce

N = 100

def sum_sq_vs_sq_sum():
    sum_of_sq = 0
    for i in range(1, N + 1):
        sum_of_sq += i ** 2
    sq_of_sum = (N * (N + 1) // 2) ** 2
    return abs(sum_of_sq - sq_of_sum)

if __name__ == "__main__":
    print(f"Result = {sum_sq_vs_sq_sum()}")
