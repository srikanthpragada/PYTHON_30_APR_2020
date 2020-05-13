nums = [10, 11, 15, 50, 35, 55]

for n in filter(lambda n : n % 2 == 0,nums):
     print(n)

for n in filter(lambda n : n > 25 ,nums):
     print(n)
