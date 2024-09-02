prev = 1
curr = 2
result = 0

while curr <= 4e6:
    result += (curr if curr % 2 == 0 else 0)
    next = prev + curr
    prev = curr
    curr = next

print(f"Result: {result}")
