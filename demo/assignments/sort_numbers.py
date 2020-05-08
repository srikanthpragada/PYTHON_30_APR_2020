# Take numbers until 0 and display them in sorted order


nums = []
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    nums.append(num)

print("Sorted Numbers :", sorted(nums))
