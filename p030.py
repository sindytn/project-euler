"""
Compute the sum of all numbers that can be expressed as the sum of the 5th power of its 
digits.

Approach:
First we find the range of numbers to check. Let's say the number is 5 digits and every 
digit was 9. Then the sum of fifth powers is 5 * (9 ** 5) = 295245 < 99999. So any number
that satisfies our condition must be less than 295245. We set this as our stopping 
condition.

Next we use brute force to check all the numbers within this range, keeping track of the
ones that satisfy our condition, and returning the sum at the end.
"""

POWER = 5
MAX = 9 ** 5 * 5

def digit_fifth_powers():
    nums = []
    for n in range(2, MAX):     # Exclude 1 since 1 = 1 ** 4 is not a sum
        digits = [int(d) for d in list(str(n))]
        if sum([d ** POWER for d in digits]) == n:
            nums.append(n)
    print(f"{nums=}")
    return sum(nums)

if __name__ == "__main__":
    print(f"Result = {digit_fifth_powers()}")