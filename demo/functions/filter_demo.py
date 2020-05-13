def iseven(n):
    return n % 2 == 0


nums = [10, 11, 15, 50, 35, 55]

total = 0
for n in nums:
    if n % 2 == 0:
        total += n

print(total)

print(sum(filter(iseven, nums)))

# for n in filter(iseven,nums):
#     print(n)
