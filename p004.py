'''
Computes the largest palindrome which is the product of two 3-digit numbers.
'''
MAX_DIGITS = 10  # Longest palindrome we are considering

def is_palindrome(n):
    num_digits = None
    for i in range(MAX_DIGITS, 1, -1):
        if int(n / 10 ** i) > 0:
            num_digits = i + 1
            break
    for i in range(num_digits):
        if not (int(n / 10 ** (num_digits - i - 1) % 10) == int(n / 10 ** i) % 10):
            return False
    return True

# Mr. J's more elegant approach
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

def largest_palindrome():
    palindromes = {}
    for a in range(100, 1000):
        for b in range(a, 1000):
            prod = a * b
            if is_palindrome(prod):
                palindromes[prod] = (a, b)
    result = max(palindromes.keys())
    print(f"Largest palindrome: {palindromes[result][0]} * {palindromes[result][1]} = {result}")

if __name__ == "__main__":
    largest_palindrome()
