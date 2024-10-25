"""
Find the perimeter describing the largest number of right triangles with integer edge lengths.

Approach:
By Pythagorean's theorem we know that for three edges a, b, and c, a^2+b^2=c^2. 
Furthermore the hypotenuse is the longest edge of a right triangle. So if we sort a and 
b in ascending order, a < b < c. This allows us to reduce the pool of candidates to 
check for a, b, and c; a < p / 3, a < b < (p - a) / 2, c = p - a - b. We iterate through 
all such a, b, and c to find the solutions for each perimeter and return the one with 
the maximum.
"""

MAX_PERIMETER = 1000

def integer_right_triangles():
    solutions_per_perimeter = {}
    for perimeter in range(3, MAX_PERIMETER + 1):
        solutions = []
        for a in range(1, perimeter // 3 + 1):
            for b in range(a, (perimeter - a) // 2 + 1):
                c = perimeter - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    solutions.append((a, b, c))
        if solutions:
            solutions_per_perimeter[perimeter] = solutions
    return max(solutions_per_perimeter.items(), key=lambda item: len(item[1]))[0]

if __name__ == "__main__":
    print(f"Result = {integer_right_triangles()}")