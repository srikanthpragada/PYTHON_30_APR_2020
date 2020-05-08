import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 100))

for n in sorted(nums):
    print(n, end=' ')
