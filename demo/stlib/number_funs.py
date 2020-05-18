# Module with functions related to numbers

PI = 22 / 7


def iseven(n):
    """
    Returns true if number is even otherwise false

    :param n: number to check
    :return: boolean

    """
    return n % 2 == 0


def isprime(n):
    return False


# Execute only when run as script
if __name__ == '__main__':
    print("Running number_funs module!")
