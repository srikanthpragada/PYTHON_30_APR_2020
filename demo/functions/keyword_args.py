def process(**args):
    pass


def fun(*values, **keywords):
    if 'operation' in keywords:
        op = keywords['operation']
    else:
        op = 'sum'

    if op == 'sum':
        return sum(values)
    elif op == 'avg':
        return sum(values) / len(values)
    else:
        raise ValueError('Invalid operation')


process(a=10, b=20, c=30)
print(fun(10, 20, 30, operation='avg'))
