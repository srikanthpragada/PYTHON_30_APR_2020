
s = "Programming is fun"

for c in sorted(set(s)):
    print(f"{c} - {s.count(c)}")