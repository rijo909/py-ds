# Create a Product class with the following:
# • Object variables:
# ► name (string)
# ► price (float)
# ► stock (integer, default is 0)
#
# • Methods: ► add_stock(quantity): Increases the stock by quantity.
# sell_product(quantity): Decreases the stock by quantity if stock is available;
# otherwise, prints an error message. ► display_info(): Prints product details.

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def add_stock(self, quantity):
        if quantity > 0:
            self.stock+=quantity
            print(f"{ quantity } stock has been deposited")
        else:
            print("invalid amount provided for deposit")
    def sell_product(self, quantity):
        if 0 < quantity <= self.stock:
            self.stock-=quantity
            print(f"{ quantity } stock has been withdrawn")
        elif quantity > self.stock:
            print("stock quantity invalid")
        else:
            print("invalid quantity provided for selling")
    def display_info(self):
        print("*==*==*==*==*===*==*==*==*==*")
        print(f"Stock name : {self.name}, Stock price : {self.price}, Stock quantity : {self.stock}")
        print("*==*==*==*==*===*==*==*==*==*")
person1 = Product("TCS", 112233, 10000)
person2 = Product("TATA", 445566, 15000)
person1.display_info()