s = "How do you do today?"

freq = {ch: s.count(ch) for ch in s if ch.isalpha()}

for c, n in freq.items():
    print(c, n)

