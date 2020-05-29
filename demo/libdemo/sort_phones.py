import re

with  open("phones.txt", "rt") as f:
    phones = set()
    for line in f:
        numbers = re.findall(r"\d+", line)
        phones = phones.union(filter(lambda n: len(n) == 10, numbers))

for phone in sorted(phones):
    print(phone)
