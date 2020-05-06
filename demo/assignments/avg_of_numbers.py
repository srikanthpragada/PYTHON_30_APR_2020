# Take numbers until 0 and display average


total = count = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    total += num
    count += 1

print(f"Average = {total // count}")
