
st = "Python 3.8 was released in 2020"

for c in filter(str.isdigit, st):
    print(c)

print("Count : ", len(list(filter(str.isdigit,st))))