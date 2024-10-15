"""
Find the number of ways to make £2 with the given coin denominations.

Approach:
Dynamic programming. Let f_c(x) be the number of ways to make x with coins of 
denomination c or lower. Let c_i be the i-th coin denomination. Then:

    f_{c_i}(x) = f_{c_{i-1}}(x) + f_{c_{i-1}}(x - c_{i-1}) + f_{c_{i-1}}(x - 2 * c_{i-1}) + ... 

We construct the DP table according to this formula and read the final value as our result.
"""

import math

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
TARGET = 200

def coin_sums(x):
    num_combos = {coin: [0 for x in range(TARGET + 1)] for coin in COINS}       # number of ways to make x using coins with keyed denomination or lower
    for c, coin in enumerate(COINS):
        # First row
        if coin == 1:
            num_combos[coin] = [1 for x in range(TARGET + 1)]
            continue

        # Subsequent rows
        for x in range(TARGET + 1):
            max_num_curr_coin = math.floor(x / coin)        # max number of coins with current row's denomination that can be used to make x
            # Init first cols
            if max_num_curr_coin < 1:
                num_combos[coin][x] = num_combos[COINS[c - 1]][x]
                continue
            for num_coins in range(max_num_curr_coin + 1):
                num_combos[coin][x] += num_combos[COINS[c - 1]][x - num_coins * coin] 
    return num_combos[COINS[-1]][TARGET]

if __name__ == "__main__":
    print(f"Result = {coin_sums(TARGET)}")