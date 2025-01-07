"""
Find the sum of 10-digit pandigital numbers where each triplet, starting from the second
digit, is divisible by the next largest prime.

Approach:
Precompute the 2- and 3-digit multiples of each prime with unique digits. Then construct
the 10-digit number efficiently with the following observations:
- There are exactly 3 disjoint triplets to be checked for divisibility: 2-4, 5-7, 8-10.
- Larger primes have fewer multiples, so work backwards through the triplets to reduce
  number of branches into for loop by using early stopping conditions.
- The first digit is whatever is remaining.
"""

primes = [2, 3, 5, 7, 11, 13, 17]


def substring_divisibility():
    # Precompute all the 3-unique-digit multiples of each prime.
    multiples = {p: [] for p in primes}
    for p in primes:
        next_multiple = p
        while next_multiple < 1000:
            # Zero-padded 2-digit multiples
            if (
                10 < next_multiple
                and next_multiple < 100
                and len(set(f"0{next_multiple}")) == 3
            ):
                multiples[p].append(f"0{next_multiple}")
            # 3-digit multiples
            if len(set(str(next_multiple))) == 3:
                multiples[p].append(str(next_multiple))
            next_multiple += p

    # Construct pandigital 10-digit number backwards since larger primes have fewer multiples.
    numbers = []
    for digits_8_10 in multiples[primes[6]]:  # 3rd disjoint triplet
        for digits_5_7 in multiples[primes[3]]:  # 2nd disjoint triplet
            # Check digits are unique
            if len(set(digits_5_7 + digits_8_10)) != 6:
                continue
            # Check overlapping triplets are multiples of primes in between
            digits_6_8 = digits_5_7[1:] + digits_8_10[:1]
            if digits_6_8 not in multiples[primes[4]]:
                continue
            digits_7_9 = digits_5_7[2:] + digits_8_10[:2]
            if digits_7_9 not in multiples[primes[5]]:
                continue
            for digits_2_4 in multiples[primes[0]]:  # Repeat with 1st disjoint triplet
                # Check digits are unique
                if len(set(digits_2_4 + digits_5_7 + digits_8_10)) != 9:
                    continue
                # Check overlapping triplets are multiples of primes in between
                digits_3_5 = digits_2_4[1:] + digits_5_7[:1]
                if digits_3_5 not in multiples[primes[1]]:
                    continue
                digits_4_6 = digits_2_4[2:] + digits_5_7[:2]
                if digits_4_6 not in multiples[primes[2]]:
                    continue
                remaining_digit = (
                    set([str(x) for x in list(range(10))])
                    - set(digits_2_4 + digits_5_7 + digits_8_10)
                ).pop()
                numbers.append(
                    int(remaining_digit + digits_2_4 + digits_5_7 + digits_8_10)
                )
    print(f"{numbers=}")
    return sum(numbers)

    # # Approach 1: Too slow. O(10!). Iterate through 10-digit numbers and check triplet divisibility for each.
    # num_pandigital = 0
    # for x in range(1023456789, 9876543210 + 1):
    #     str_x = str(x)
    #     if int(str_x[3]) not in range(0, 10, 2):
    #         continue
    #     if int(str_x[5]) not in range(0, 10, 5):
    #         continue
    #     if set(str_x) != digit_pool:
    #         continue
    #     num_pandigital += 1
    #     is_divisible = True
    #     for i in range(1, 7):
    #         substring_int = int(str_x[i: i + 3])
    #         if substring_int % primes[i - 1] != 0:
    #             is_divisible = False
    #             break
    #     if is_divisible:
    #         print(x)
    #         numbers.append(x)
    # print(numbers)
    # return sum(numbers)


if __name__ == "__main__":
    print(f"Result = {substring_divisibility()}")
