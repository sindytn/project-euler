"""
Computes the total lengths of the English representative of the numbers from 1 to N, inclusive.

Approach: 
List out the predefined numbers with special wordings, such as "eleven" which is not 
referred to as "one ten". From this starting point, track the lengths of each number 
from 1 to N as we encounter them, using seen lengths of its parts where possible. e.g. 
123 is "one hudnred and twenty-three" where the length of "twenty-three" was already
seen and stored.
"""

N = 1000

WORDS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen', 
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand'
}

def number_letter_counts():
    lengths = {k: len(v) for k, v in WORDS.items()}
    for n in range(1, N + 1):
        hundreds_digit = n // 100
        tens_digit = (n % 100) // 10
        ones_digit = n % 10

        if n in lengths:
            continue
        elif n < 100:
            length = lengths[10 * tens_digit] + lengths[ones_digit]
            lengths[n] = length
        else:
            length = lengths[hundreds_digit] + len('hundred')
            if n % 100 > 0:
                length += len('and') + lengths[n % 100]
            lengths[n] = length
    return sum(v for k, v in lengths.items() if k <= N)

if __name__ == "__main__":
    print(f"Result = {number_letter_counts()}")
