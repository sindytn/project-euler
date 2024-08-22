"""
Computes the starting number <= N with the longest Collatz sequence.

Approach:
We compute the length of the Collatz sequence for every number n starting from N. For 
speed, we store a dict to remember the Collatz sequence lengths of all numbers in the 
subsequences of n. The construction of this dict uses the fact that in the Collatz 
sequence n1 -> n2 -> n3 -> ... -> 1, len(seq(n1)) = len(seq(n2)) + 1. This dict is used 
for lookup so that when we reencounter any seen number, we don't need to recompute the 
length of the subsequence that starts with it.
"""

N = 999999

def longest_collatz_sequence():
    seq_lengths = {}
    for n in range(N, 0, -1):
        seen = []
        length = 1
        m = n
        while m != 1:
            if m in seq_lengths:
                length += seq_lengths[m]
                break
            seen.append(m)
            m = m // 2 if m % 2 == 0 else 3 * m + 1
            length += 1
        for i in range(len(seen)):
            if seen[i] <= N:
                seq_lengths[seen[i]] = length - i
    return max(seq_lengths, key=seq_lengths.get)

if __name__ == "__main__":
    print(f"Result = {longest_collatz_sequence()}")