result = 0

for i in range(1000):
    result += (i if i % 3 == 0 or i % 5 == 0 else 0)

print(f"Result {result}")