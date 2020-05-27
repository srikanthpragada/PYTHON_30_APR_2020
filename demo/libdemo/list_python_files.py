import os

root = os.walk(r"c:\classroom\apr30\demo")

for dirname, dirs, files in root:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
