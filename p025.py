"""
Compute the index of the first Fibonacci number to have the given number of digits.

Approach:
Brute force. We compute every Fibonacci number by storing and updating the previous two 
until it contains the target number of digits. Take care to store the previous values 
with temporary variables to they don't get overwritten by the new Fibonacci number.
"""

N = 1000

def n_digit_fibonacci(num_digits):
    threshold = 10 ** (num_digits - 1)
    f_k_minus_1 = 1
    f_k = 1
    k = 2
    while f_k < threshold:
        new_f_k = f_k + f_k_minus_1
        f_k_minus_1 = f_k
        f_k = new_f_k
        k += 1
    return k 

if __name__ == "__main__":
    print(f"Result = {n_digit_fibonacci(N)}")