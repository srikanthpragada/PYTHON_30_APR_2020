class Product:
    # static attribute or class attribute
    taxrate = 15

    @classmethod
    def create_product(cls,name):
        p = cls(name)
        p.price = p.qty = 0
        return p


    @staticmethod   # Decorator
    def set_taxrate(newrate):
        Product.taxrate = newrate

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
        return self.price + (self.price * Product.taxrate / 100)


p1 = Product("Bose Headphones", 25000)  # Create an object
# print(p1.supplier)
p1.print_details()
print('Net price : ', p1.net_price())

Product.set_taxrate(20)   # Call static method

p2 = Product("Mac Air",200000)  # Create an object
print('Net price : ', p2.net_price())

# Create a product object

p3 = Product.create_product("Dell Laptop")
p3.print_details()
