import re

with open(r"c:\classroom\old_man.txt") as f:
    words = {}

    content = f.read()
    doc_words = re.findall(r"\w+", content.upper())
    # print(doc_words)

    for word in doc_words:
        if word in words:  # word is ready present
            words[word] += 1  # Increment count
        else:
            words[word] = 1

    for word, count in sorted(words.items()):
        print(f"{word:15} - {count:3}")
