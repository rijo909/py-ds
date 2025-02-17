# what is functional programming
# What is higher order functions
# Purpose of map, filter and reduce functions

# What is Functional Programming?
# Functional programming is a programming paradigm that treats computation as the evaluation of
# mathematical functions and avoids changing state or mutable data. It emphasizes declarative code
# and uses functions as the primary building blocks of logic.
#
# Key characteristics of functional programming include:
# >> Pure functions: Functions that always produce the same output for the same input and have no
# side effects.
# >> Immutability: Data does not change; instead, new data structures are created.
# >> First-class functions: Functions can be assigned to variables, passed as arguments, or returned by other functions.
# >> Higher-order functions: Functions that take other functions as arguments or return them as results.

# map :
lst=[2, 3, 4, 5]
var1 = list(map(lambda a:a-1, lst))
var2 = list(map(lambda a:round(a**0.5, 2), lst))
# print(lst, var1, var2, sep='\n')

# Given a list of temperatures in Celsius, use map() to convert each value to Fahrenheit.
# Formula: Fahrenheit = (Celsius * 9/5) + 32
# Input: temperatures_celsius = [0, 20, 37, 100]
# Expected Output: [32.0, 68.0, 98.6, 212.0]

# map :
lst = [0, 20, 37, 100]
var1 = list(map(lambda a:(a * 9/5) + 32, lst))
print(var1)
