"""
Find the numbers under 1e6 which are palindromes in base 2 and base 10.

Approach:
Brute force. 
"""
import math

MAX_X = 1000000

def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-1 * i - 1]:
            return False
    return True

def base_2_str(base_10):
    digits = []
    remain = base_10
    for power in range(int(math.log2(base_10)), -1, -1):
        if 2 ** power <= remain:
            digits.append(1)
            remain -= 2 ** power
        else:
            digits.append(0)
    return ''.join([str(d) for d in digits])

def double_base_palindromes():
    palindromes = []
    for x in range(1, MAX_X):
        # Optimization: check base 10 first to reduce the number of conversions to base 2
        if is_palindrome(x) and is_palindrome(base_2_str(x)):
            palindromes.append(x)
    return sum(palindromes)

if __name__ == "__main__":
    print(f"Result = {double_base_palindromes()}")