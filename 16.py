"""
Computes the sum of the digits of 2^N.

Approach: Brute force. Two ways:
A) Sum digits by taking the rightmost digit by mod 10, then shifting the remaining by dividing by 10.
B) Convert the 2^N to a string, split out the chars, convert it back to int, then add.
"""

N = 1000

def power_digits_sum():
    sum = 0
    n = 2 ** N
    while n >= 10:
        sum += n % 10
        n //= 10
    sum += n
    return sum

def power_digits_sum_str():
    return sum([int(x) for x in list(str(2 ** N))])

if __name__ == "__main__":
    # print(f"Result = {power_digits_sum()}")
    print(f"Result = {power_digits_sum_str()}")