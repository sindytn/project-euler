'''
Approach: Consider the prime factorization of N. Sort and iteratively remove all powers 
of prime factors. Since the factors were sorted, the last one removed is the largest. 
When the last factor is removed, the quotient becomes one, so we can use this as our 
stopping condition.
'''

N = 600851475143

def largest_prime_factor(n):
    dividend = n
    divisor = 2
    result = 1  # The last divisor

    while result < dividend:
        if dividend % divisor == 0:
            result = divisor
        while dividend % divisor == 0:
            dividend /= divisor
        divisor += 1
    return result

if __name__ == "__main__":
    print(f"result = {largest_prime_factor(N)}")
