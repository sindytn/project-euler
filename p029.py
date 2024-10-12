"""
Find the number of distinct powers a ** b for all a and b between 2 and 100.

Approach:
Brute force. The implementation is simplified by using Python's set, which omits 
duplicate items by definition.
"""


MAX_A = 100
MAX_B = 100

def distinct_powers():
    seen = set([])
    for a in range(2, MAX_A + 1):
        for b in range(2, MAX_B + 1):
            curr = a ** b
            if curr not in seen:
                seen.add(curr)
    return len(seen)

if __name__ == "__main__":
    print(f"Result = {distinct_powers()}")