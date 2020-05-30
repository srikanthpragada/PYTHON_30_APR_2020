import re

with open(r"c:\classroom\test.txt", "rt") as f:
    content = f.read()
    content = re.sub(r" {2,}", ' ', content)  # Replace two or more spaces with one
    content = re.sub(r"\n{2,}", r'\n', content)  # Replace two or more \n with one

    tf = open(r"c:\classroom\new_test.txt", "wt")
    tf.write(content)
    tf.close()
