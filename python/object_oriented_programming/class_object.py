class Vehicle: # identifiers rule for naming class
    pass
obj1 = Vehicle() # object of class
# print(type(obj1))
# print(obj1)

class Vehicle:
    company = "BMW" # class variable
    def __init__(self, model_name, model_year):
        self.model = model_name # object variable or instance variable
        self.year = model_year # object variable
obj1 = Vehicle("abc", "2024")
obj2 = Vehicle("xyz", "2022")
# print(obj1.company, obj1.model, obj1.year)
# print(obj2.company, obj2.model, obj2.year)

# create a BankAccount class
# add the following
# class variable :
#     bank_name
# Instance variable:
#     account_holder
#     account_num
#     balance

class BankAccount:
    bank_name = "SIB"
    def __init__(self, bank_acc_account_holder, bank_acc_account_num, bank_acc_balance):
        self.account_holder = bank_acc_account_holder
        self.account_num = bank_acc_account_num
        self.balance = bank_acc_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"{ amount } amount has been deposited")
        else:
            print("invalid amount provided for deposit")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"{ amount } amount has been withdrawn")
        elif amount > self.balance:
            print("Balance insufficient")
        else:
            print("invalid amount provided for withdrawal")
    def acc_details(self):
        print("*==*==*==*==*===*==*==*==*==*")
        print(f"Account holder name : {self.account_holder}, Account holder name : {self.account_num}, Account holder name : {self.balance}")
        print("*==*==*==*==*===*==*==*==*==*")
person1 = BankAccount("Rijo", 112233, 10000)
person2 = BankAccount("Lisa", 445566, 15000)
# print(person1.acc_details())
# print(person2.acc_details())
# person1.deposit(200)
# print(person1.acc_details())
# print(person2.acc_details())
# person2.withdraw(200)
# print(person2.acc_details())
# person2.withdraw(200000)

# Create a class ShoppingCart with the following functionality:
# Attributes:
# 1. items: A dictionary to store items and their quantities ({item_name: quantity}).
# 2. prices: A dictionary to store items and their prices ({item_name: price}).
#
# Methods:
# 1. _init_(): Initializes the cart as empty (items and prices are empty dictionaries).
# 2. add_item(item_name, quantity, price): Adds an item to the cart with the given quantity and price.
# If the item already exists, increase its quantity.
# 3. remove_item(item_name, quantity): Removes the specified quantity of an item from the cart.
# If the quantity becomes zero or negative, remove the item entirely.
# 4. view_cart(): Displays all items in the cart with their quantities and prices, and calculates the total cost.
# 5. checkout(): Prints the total amount to pay, clears the cart, and ends the shopping session.
print()
class ShoppingCart:
    def __init__(self):
        self.items={}
        self.prices={}
    def add_item(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name]+=quantity
        else:
            self.items[item_name]=quantity
            self.prices[item_name]=price
    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if quantity>=self.items[item_name]:
                del self.items[item_name]
                del self.prices[item_name]
                print(f"{item_name} removed from the cart")
            else:
                self.items[item_name]-=quantity
        else:
            print("Item Not Found")
    def view_cart(self):
        sum_cart = 0
        print("\nView Cart :")
        print("==============")
        for i in self.items:
            print(f"""{str(i).capitalize()} -- Qty:{self.items[i]} @ Rs.{self.prices[i]}(Rate) -- Rs.{self.items[i]*self.prices[i]}""")
            sum_cart += self.items[i] * self.prices[i]
        print(
            f"Total Rs.{sum_cart}")
        if len(self.items) == 0:
            print("Cart is empty\nTotal Cost = 0")
    def checkout(self):
        sum_cart = 0
        print("\nCheckout :")
        print("==============")
        if len(self.items) == 0:
            print("Cart is empty\nTotal Cost = 0")
        else:
            for i in self.items:
                sum_cart += self.items[i]*self.prices[i]
            print(
                f"""Please pay sum total of Rs.{sum_cart} at the checkout counter""")
cart1 = ShoppingCart()
cart1.add_item("pen", 10, 30)
cart1.remove_item("pen", 2)
cart1.add_item("toothpaste", 1, 50)
cart1.add_item("rubber", 5, 5)
cart1.add_item("pen", 3, 30)
cart1.view_cart()
cart1.checkout()
# print(cart1)
