"""
Computes the "score" of the names in a given text file.

Approach:
Sort the names to get the alphabetical position of each. Precompute the char to num 
mapping {A: 1, B: 2, ..., Z: 26}; use this mapping to compute the sub-score of each 
individual name. Multiply the alphabetical position by sub-score and sum to get the 
final result.
"""

import argparse
import csv

CHAR_TO_NUM = {chr(ord('A') + i): i + 1 for i in range(26)}

def names_scores(names):
    result = 0
    for i, name in enumerate(sorted(names)):
        result += sum([CHAR_TO_NUM[c] for c in list(name)]) * (i + 1)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='Path to the downloaded txt file containing names to process.')
    args = parser.parse_args()

    # Load and parse file
    names = []
    with open(args.filepath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            names += row

    print(f"Result = {names_scores(names)}")

