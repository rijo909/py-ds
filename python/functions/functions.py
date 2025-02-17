# # defining the function with its code block and
# # returning it to caller using return
# def demo_functions():
#     a = input("Enter a number : ")
#     b = input("Enter another number : ")
#     return f'sum is : {int(a) + int(b)}'
# c = demo_functions() # function processed value returned value into c
# print(c) # value of c printed

# Define a function greet_user
# inside the function, take the input user name and
# greet the user with name
# Hello {usr_name}, good morning. Have a nice day!

# def greet_user():
#     usr_name = input("Please enter your name : ")
#     print(f'Hello {usr_name.title()}, good morning. Have a nice day!')
# greet_user()

# def even_or_not(num1):
#     if (num1.isdigit()):
#         num1 = int(num1)
#         if num1%2 == 0:
#             return True
#         else:
#             return False
#     else:
#         print("Enter a Number not a character")
# num1 = input("Enter a number : ")
# func_response = even_or_not(num1)
# if func_response == True or func_response == False:
#     print(func_response)

# # Check if palindrome or not
# # create a function to check if the input string is palindrome or not
# def usr_palindrome(str1):
#     if str1.lower() == str1.lower()[::-1]:
#         return True
#     else:
#         return False
# str1 = input("Enter a word : ")
# print(usr_palindrome(str1))

# #1 Write a function that takes two numbers a and b where
# # b has a default value of 2.
# # Function should return the product of a and b
# # product_two_numbers
# def product_two_numbers(a, b=2):
#     return a*b
# print(product_two_numbers(3, 5))


# #2 Write function that takes one number and check if it is armstrong
# # number or not. IF armstrong return True, else return False.
# def usr_armstrong_func():
#     num1 = int(input("Enter a number : "))
#     str1 = str(num1)
#     digits_count = len(str1)
#     c=0
#     for i in str1:
#         c+=int(i)**digits_count
#     if c==num1:
#         return True
#     else:
#         return False
# print(usr_armstrong_func())

# # Write a Python function called calculate total that:
# # 1. Takes a dictionary as input, where the keys are product
# # names and the values are tuples of (quantity, unit price).
# # 2. Calculates the total cost of all products in the dictionary.
# # 3. Returns the total sum of all products.
# def total_cost(dict1:dict): # dictionary expected in the function using :dict
#     sum1 = 0
#     total_sum = 0
#     for i, j in dict1.values():
#         total_sum += i*j
#     return total_sum
# dict1={
#             "apple":(12, 3),
#             "orange": (8, 5),
#             "grape": (45, 60)
#         }
# print(f'Total Cost : {total_cost(dict1)}')

# converting list with tupple pair to dictionary
# l1= [(2, 3), (5, 1), (4, 4)]
# print(dict(l1))
# l1= [([2, 3], 2), (5, 1), (4, 4)] # not possible, as data are not pairs
# print(dict(l1))

# factorial of a given number
def num_fact(num1:int):
    fact_num = 1
    for i in range(num1):
        fact_num*=num1
        num1-=1
    return fact_num
# num1 = input("Enter a number to find its factorial : ")
# print(num_fact(num1))

# count vowels function:
def count_vowels(str1:str):
    c1 = 0
    for i in str1:
        if i.lower() in 'aeiou':
            c1 += 1
    return c1
# str1 = input("Enter a string : ")
# print(f'Number of vowels : {count_vowels(str1)}')

# fibonacci series function:
def fibonacci_num(num1:int):
    lst_fib = [0, 1]
    for i in range(num1 - 2):
        lst_fib.append(lst_fib[-1] + lst_fib[-2])
    for i, j in enumerate(lst_fib):
        if i != len(lst_fib) - 1:
            print(j, end=", ")
        else:
            print(j)
# num1 = int(input("Enter the number of series required : "))
# print(fibonacci_num(num1))

# prime number function
def is_prime(num1:int):
    c1=0
    for i in range(2, num1+1):
        if num1%i == 0:
            c1+=1
    if c1 == 1:
        return True
    else:
        return False
# num1 = int(input("Enter number to check if prime : "))
# print(is_prime(num1))

# common elements in two lists, return list from function
def common_list_ele(a:list, b:list):
    return list(set(a).intersection(set(b)))
# print(common_list_ele([2,3,4,5], [4,5,6]))

#6. Write a function longest_word that returns the longest word in a given sentence.
# eg. "I love python programming"
# Output:"programming"
def longest_word(str1:str):
    str1_list = str1.split()
    max_word = ""
    for i in str1_list:
        if len(i) > len(max_word):
           max_word = i
    return max_word
str1 = input("Enter a sentence : ")
print(longest_word(str1))