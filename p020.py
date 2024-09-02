"""
Computes the sum of the digits of N!

Approach: Brute force. After computing N!, we can cast the product to a string to split 
out the digits and then take the sum. 
"""

N = 100

def factorial_digit_sum():
    product = 1
    for n in range(1, N + 1):
        product *= n
    return sum([int(n) for n in list(str(product))])

if __name__ == "__main__":
    print(f"Result = {factorial_digit_sum()}")