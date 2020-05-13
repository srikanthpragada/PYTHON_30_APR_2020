def task(a, b, operation):
    print(operation(a, b))


def add(n1, n2):
    return n1 + n2


def product(n1, n2):
    return n1 * n2


task(10, 20, add)
task(20,50, product)
