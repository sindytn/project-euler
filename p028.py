"""
Compute the sum of the diagonals of the grid formed by clockwise-spiraled consecutive 
numbers.

Approach: 
We notice a pattern as we move towards outer layers of the spiral. Namely,
- The dimension starts at 1x1 and increases by 2 each layer.
- The difference between each clockwise-consecutive numbers in the diagonal of each 
  layer is the same; it starts at 2 and increases by 2 each layer. 

    dimension:  1 ---3---  ----5----  ...
    diagonal:   1 3 5 7 9 13 17 21 25 ...
    delta:      ----2--- -----4-----  ...

We track each diagonal number and use this pattern to construct the next one. We also 
track the cumulative sum. O(d) where d := DIMENSION.
"""

DIMENSION = 1001

def spiral_diagonals():
    sum_diagonal = 1
    last_seen = 1
    for i in range(2, DIMENSION, 2):
        for j in range(4):
            last_seen += i
            sum_diagonal += last_seen 
    return sum_diagonal

if __name__ == "__main__":
    print(f"Result = {spiral_diagonals()}")