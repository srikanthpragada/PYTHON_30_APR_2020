# Generator to yield values from 1 to 5
def numbers():
    for n in range(1,6):
        yield n


n = numbers()
print(type(n))

print( next(n))