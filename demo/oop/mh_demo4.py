class A:
    def process(self):
        print('method process() in Base')


class B(A):
    def process(self):
        print('method process() in B')


class C(B, A):
    pass


obj = C()
print(C.mro())
