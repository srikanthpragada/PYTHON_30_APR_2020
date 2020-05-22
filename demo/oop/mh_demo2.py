class Base:
    def process(self):
        print('method process() in Base')

class A(Base):
    pass


class B:
    def process(self):
        print('method process() in B')


class C(A, B):
    def task(self):
        print('method process() in C')


obj = C()
obj.process()
