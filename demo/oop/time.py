class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()

    def __gt__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __int__(self):
        return self.total_seconds()

    def __add__(self, seconds):
        if isinstance(seconds, int):
            t = Time(self.h, self.m, self.s + seconds)
            return t
        else:
            return self


t = Time(10, 20, 30)
t2 = Time(10, 20, 30)
t3 = Time(11, 0, 0)
# print(t)
# print(str(t))
# print(t.__str__())
# print(t == t2)  # t.__eq__(t2)
# print(t3 > t2)  # t3.__gt__(t2)
# print(int(t))
t4 = t3 + 30
print(t4)
t4 = t3 + "Abc"
