class Marks_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def __next__(self):
        if len(self.data) == self.pos:
            raise StopIteration

        value = self.data[self.pos]
        self.pos += 1
        return value


class Marks:
    def __init__(self):
        self.data = [50, 40, 60, 70, 80]

    def __iter__(self):
        obj = Marks_Iterator(self.data)
        return obj


m = Marks()
mi1 = iter(m)
mi2 = iter(m)

print(mi1.__next__())
print(mi2.__next__())
