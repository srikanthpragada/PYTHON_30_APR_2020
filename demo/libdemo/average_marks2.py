with  open("marks.txt", "rt") as file:
    lines = file.readlines()
    total = sum(map(int, lines))
    print('Average Marks : ', total / len(lines))
