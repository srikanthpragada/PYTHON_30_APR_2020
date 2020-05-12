def greet(message='Hi', person=None):
    if person:
        print(message, person)
    else:
        print(message)


greet("Hi", "Andy")
greet("Hello")
greet(person="Andy")
greet(person="Scott", message="Hello")