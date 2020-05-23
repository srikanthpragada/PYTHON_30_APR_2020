l = [1, 2, 3]

# l.add(4)
try:
    v = int(input("Enter a number :"))
    print(100/v)
except ValueError:
    print("Invalid number!")
else:
    print("Success")
finally:
    print("Finally block")


print("The End!")

