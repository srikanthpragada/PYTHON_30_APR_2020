import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age}"


p1 = Person("Mike", 30)
print(json.dumps(p1.__dict__))
