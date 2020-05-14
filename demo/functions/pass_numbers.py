
def zero(n):
    print("Before change : ", id(n))
    n = 0
    print("After change : ", id(n))

a = 100
print("Address of a before ", id(a))
zero(a)
print("Address of a after ", id(a))
print(a)
