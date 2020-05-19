class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.__balance = balance   # Private attribute

    def print_details(self):
        print(f"Account no.    : {self.acno}")
        print(f"Account holder : {self.ahname}")
        print(f"Current balance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


a1 = SavingsAccount(1, 'Jason', 10000)
a1.deposit(5000)
# a1._SavingsAccount__balance = 1000000
print(a1.__dict__)
a1.print_details()