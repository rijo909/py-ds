from functools import reduce
from math import trunc

# ---
# Exercise 1: Squares of Numbers
# Task: Use map() to square each number in a given list.
# Input: [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]

num_list = [1, 2, 3, 4, 5]
result_list = list(map(lambda a:a**2, num_list))
print(result_list)

# ---
# Exercise 2: Convert Strings to Uppercase
# Task: Use map() to convert all the strings in a list to uppercase.
# Input: ['apple', 'banana', 'cherry']
# Output: ['APPLE', 'BANANA', 'CHERRY']
str_list = ['apple', 'banana', 'cherry']
result_list = list(map(lambda a:str(a).upper(), str_list))
print(result_list)

# ---
# Exercise 3: Even Numbers Filter
# Task: Use filter() to extract only the even numbers from a list.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [2, 4, 6, 8]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_list = list(filter(lambda a:a%2 == 0, num_list))
print(result_list)

# ---
# Exercise 4: Filter Names Starting with 'A'
# Task: Use filter() to select names that start with the letter 'A'.
# Input: ['Alice', 'Bob', 'Anna', 'Mark', 'Anil']
# Output: ['Alice', 'Anna', 'Anil']
str_list = ['Alice', 'Bob', 'Anna', 'Mark', 'Anil']
result_list = list(filter(lambda a:a[0] == 'A', str_list))
print(result_list)

# ---
# Exercise 5: Sum of List Elements
# Task: Use reduce() to calculate the sum of all numbers in a list.
# Input: [1, 2, 3, 4, 5]
# Output: 15
num_list = [1, 2, 3, 4, 5]
result = reduce(lambda a,b:a+b, num_list)
print(result)

# ---
# Exercise 6: Product of List Elements
# Task: Use reduce() to compute the product of all numbers in a list.
# Input: [1, 2, 3, 4]
# Output: 24
num_list = [1, 2, 3, 4]
result = reduce(lambda a,b:a*b, num_list)
print(result)

# ---
# Exercise 7: Combine Map and Filter - Square Evens
# Task: Use filter() to select even numbers, and then map() to square them.
# Input: [1, 2, 3, 4, 5, 6]
# Output: [4, 16, 36]
num_list = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x:x**2, filter(lambda x:x%2 == 0, num_list)))
print(result)

# ---
# Exercise 8: Find the Longest String
# Task: Use reduce() to find the longest string in a list.
# Input: ['cat', 'elephant', 'dog', 'hippopotamus']
# Output: 'hippopotamus'
str_list = ['cat', 'elephant', 'dog', 'hippopotamus']
result = reduce(lambda a,b:a if len(a)> len(b) else b, str_list)
print(result)
# ---
# Exercise 9: Count Names with 'e'
# Task: Use filter() to count names containing the letter 'e'.
# Input: ['Steve', 'Alice', 'Tom', 'Eve']
# Output: 3
str_list = ['Alice', 'Bob', 'Anna', 'Mark', 'Anil']
c1=0
result_list = len(list(filter(lambda a: 'e' in a.lower(), str_list)))
print(result_list)
# ---
# Exercise 10: Reverse Strings in a List
# Task: Use map() to reverse each string in a list.
# Input: ['hello', 'world', 'python']
# Output: ['olleh', 'dlrow', 'nohtyp']
str_list = ['hello', 'world', 'python']
result_list = list(map(lambda a:a[::-1], str_list))
print(result_list)

# ---
# Exercise 11: Sum of Squares Using Reduce
# Task: Use map() to square numbers and reduce() to find the sum of squares.
# Input: [1, 2, 3, 4]
# Output: 30
num_list = [1, 2, 3, 4]
result = reduce(lambda a,b:a+b, list(map(lambda a:a**2, num_list)))
print(result)

# ---
# Exercise 12: Check for All Even Numbers
# Task: Use filter() and reduce() to check if all numbers in the list are even.
# Input: [2, 4, 6, 8]
# Output: True
# num_list = [1, 2, 3, 4]
num_list = [2, 4, 6, 8]
init_sum = reduce(lambda a,b:a+b, num_list)
result = list(filter(lambda a:a%2 == 0, num_list))
fin_sum = reduce(lambda a,b:a+b, list(filter(lambda a:1 if a%2 == 0 else 0, num_list)))
if init_sum == fin_sum:
    print(True)
else:
    print(False)