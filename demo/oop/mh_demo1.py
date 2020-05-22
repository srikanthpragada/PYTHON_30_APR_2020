class A:
    def process(self):
        print('method process() in A')


class B:
    def process(self):
        print('method process() in B')


class C(A, B):
    def task(self):
        print('method process() in C')


obj = C()
obj.process()
