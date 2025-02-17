# Class A and Class B have the following students:
# • class_a = {"John", "Alice", "Bob", "Diana"}
# • class_b = {"Alice", "Bob", "Eve", "Frank"}
# Find the students who are in either Class A or Class B but not in both
class_a = {"John", "Alice", "Bob", "Diana"}
class_b = {"Alice", "Bob", "Eve", "Frank"}
print(class_a.symmetric_difference(class_b))

# A store has a list of products in stock and a list of sold products:
# • in_stock = {"apples", "bananas", "grapes", "oranges"} • sold = {"bananas", "oranges"}
# Find the products that are still in stock but not sold.
in_stock = {"apples", "bananas", "grapes", "oranges"}
sold = {"bananas", "oranges"}
print(in_stock.difference(sold))
