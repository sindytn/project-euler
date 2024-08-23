"""
Compute the number of right/down-moving paths from the top left to bottom right corner 
of an N x N grid.

Approach:
Dynamic programming. The number of paths to any point in the lattice is the sum of the 
number of paths to the point one left and one above it. Compupting these starting from 
the top left to bottom right gives us the desired result in the bottom right.
"""

N = 20

def lattice_paths():
    lattice = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for r, row in enumerate(lattice):
        for c, col in enumerate(row):
            if r == 0:
                lattice[r][c] = 0 if c == 0 else 1
            else:
                lattice[r][c] = 1 if c == 0 else lattice[r][c - 1] + lattice[r - 1][c]
    return lattice[-1][-1]

if __name__ == "__main__":
    print(f"Result = {lattice_paths()}")