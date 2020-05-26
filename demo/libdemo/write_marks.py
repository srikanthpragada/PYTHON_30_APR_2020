
f = open("marks.txt","wt")

while True:
    marks = int(input("Enter marks [-1 to stop]:"))
    if marks == -1:
        break

    f.write(str(marks) + "\n")


f.close()
print('Successfully wrote marks to file!')


