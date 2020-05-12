def add(n1, n2):
    return n1 + n2


def calculate_interest(amount, rate=12):
    return amount * rate / 100


print(add(10, 20))
print(calculate_interest(10000, 14.5))
print(calculate_interest(15000))
print(calculate_interest(rate=15, amount=15000))
