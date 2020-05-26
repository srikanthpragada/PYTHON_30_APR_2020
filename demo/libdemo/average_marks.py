file = open("marks.txt", "rt")

total = 0
lines = file.readlines()

for line in lines:
    total += int(line)

file.close()
print('Average Marks : ', total / len(lines))
