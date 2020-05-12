# Overloading

def add(n1, n2):
    return n1 + n2


print(type(add))
print(id(add))


def add(n1, n2, n3):
    return n1 + n2 + n3


print(type(add))
print(id(add))

print(add(10, 20))
print(add(1, 3, 4))
