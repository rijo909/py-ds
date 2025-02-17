# 1.Create a dictionary that groups words from a list by their lengths.
# Example Input: ["cat", "dog", "apple", "banana"]
# Output: {3: ["cat", "dog"], 5: ["apple"], 6: ["banana"]}
words = ["cat", "dog", "apple", "banana"]
grouped_words = {}
for word in words:
    length = len(word)
    grouped_words.setdefault(length, []).append(word)
print("Grouped words by length:", grouped_words)

# 2.students = {"John": 85, "Alice": 78, "Bob": 92, "Clara": 88, "Daisy": 72}
students = {"John": 85, "Alice": 78, "Bob": 92, "Clara": 88, "Daisy": 72}
# Questions:
# a. Calculate and print the average score
average_score = sum(students.values()) / len(students)
print("Average score:", average_score)
# b. Find the names of students who scored above 80
above_80 = [name for name, score in students.items() if score > 80]
print("Students scoring above 80:", above_80)
# c. Add a new student "Eve" with a score of 95
students["Eve"] = 95
print("Updated students dictionary:", students)
# d. Sort the dictionary by students' names
sorted_students = dict(sorted(students.items()))
print("Sorted students dictionary:", sorted_students)
# e. Invert the dictionary
inverted_students = {score: name for name, score in students.items()}
print("Inverted students dictionary:", inverted_students)

# 3.products = {"milk": 1.5, "bread": 2.0, "butter": 3.5, "cheese": 4.0}
products = {"milk": 1.5, "bread": 2.0, "butter": 3.5, "cheese": 4.0}
# Questions:
# a. Calculate the total cost of all products
total_cost = sum(products.values())
print("Total cost of all products:", total_cost)
# b. Add a new product "eggs" with a price of 2.5
products["eggs"] = 2.5
print("Updated products dictionary:", products)
# c. Find the most expensive product
most_expensive_product = max(products, key=products.get)
print("Most expensive product:", most_expensive_product)
# d. Create a new dictionary with prices rounded to the nearest integer
rounded_prices = {product: round(price) for product, price in products.items()}
print("Products with rounded prices:", rounded_prices)
# e. Remove all products priced below 2.0
filtered_products = {product: price for product, price in products.items() if price >= 2.0}
print("Filtered products dictionary:", filtered_products)

# 4.Count Word Frequency in a String Using a Dictionary.
# text = "hello world hello everyone welcome to the world of programming"
text = "hello world hello everyone welcome to the world of programming"
words = text.split()
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Word frequency:", word_frequency)
