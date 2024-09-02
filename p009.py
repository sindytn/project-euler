'''
Finds the Pythagorean triplet summing to 1000.

Approach: We are given that there is only one such solution. Iteratively check all 
possibilities for a and b such that a^2 + b^2 = c^2. We note two facts about right 
triangles: 
- We only need to check up to N/2 for a and b because the length of each edge of a 
  triangle must be strictly less than the sum of the other two. 
- We don't need to check a == b because a right triangle cannot be isosceles
'''

N = 1000

def pythagorean_triplet():
    for a in range(N//2):
        for b in range(a):
            if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
                print(f"{a} * {b} * {1000 - a - b} = {a * b * (1000 - a - b)}")
                return

if __name__ == "__main__":
    pythagorean_triplet()