class Product:
    # Constructor
    def __init__(self, name, price=None):
        # Object attributes
        self.name = name
        self.price = price
        self.qoh = 0

    # Method
    def print_details(self):
        print("Name : ", self.name)
        print("Price: ", self.price)

    def net_price(self):
        return self.price + (self.price * 15 / 100)


p1 = Product("Bose Headphones", 25000)  # Create an object
p1.print_details()
print('Net price : ', p1.net_price())

p2 = Product("Mac Air")  # Create an object
p2.price = 150000
p2.print_details()

