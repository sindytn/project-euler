"""
Find the number d < 1000 such that 1/d has the longest reptend.

Approach:
Implement long division while tracking all the seen remainders and digits of the 
quotient. The quotient digits start to repeat once we see any remainder a second time. 
So the length of the reptend is the number of steps since we last saw this remainder.
"""

MAX_DENOMINATOR = 1000

def reciprocal_cycles(max_denominator):
    repeats = {}  # Dict of d: [<repeated_digits>]
    for d in range(2, max_denominator + 1):
        decimal_digits = []
        curr_remainder = 1 
        remainders = [curr_remainder]
        while curr_remainder != 0:
            next_digit = (curr_remainder * 10) // d
            decimal_digits.append(next_digit)
            curr_remainder = curr_remainder * 10 - d * next_digit
            if curr_remainder in remainders:
                repeated_digits = ''.join(str(d) for d in decimal_digits[remainders.index(curr_remainder):])
                repeats[d] = repeated_digits
                # print(f"Repeated digits in 1/{d} : {repeated_digits}")  # Debug
                break
            remainders.append(curr_remainder)
    lengths = {d: len(repeats[d]) for d in repeats}
    return max(lengths, key=lengths.get)

if __name__ == "__main__":
    print(f"Result = {reciprocal_cycles(MAX_DENOMINATOR)}")
