def hello():
    print("Hello!")


def greet(message='Hi', person=None):
    if person:
        print(message, person)
    else:
        print(message)


hello()
greet()
greet("Good Morning")
greet("Good Bye","Tom")
