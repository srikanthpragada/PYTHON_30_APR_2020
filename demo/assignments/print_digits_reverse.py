s = "abc 123 xyz 984"
for c in reversed(s):  # s[::-1]
    if c.isdigit():
        print(c)
