import os
import sys


def file_contains_string(filename, search_string):
    with open(filename, "rt") as f:
        content = f.read()
        if content.find(search_string) >= 0:
            return True
        else:
            return False


if len(sys.argv) < 2:
    print("Usage : python search_python_files.py  search_string  [root_dir]")
    sys.exit(0)

search_string = sys.argv[1]
# If no root is provided then take current directory
if len(sys.argv) > 2:
    root_dir = sys.argv[2]
else:
    root_dir = os.getcwd()

root = os.walk(root_dir)

for dirname, dirs, files in root:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if file_contains_string(filename, search_string):
                print(filename)
