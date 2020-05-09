# Take names and display unique names in sorted order

names = set()
while True:
    name = input("Enter a number [end to stop] :")
    if name == "end":
        break

    names.add(name)

print(sorted(names))

