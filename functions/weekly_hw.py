# PYTHON PRACTICE QUESTIONS

# 1.Write a Python program to determine whether a given list of integers contains exactly
# two occurrences of the number 19 and at least three occurrences of the number 5. If both
# conditions are satisfied, return True otherwise, return False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True
def check_occurrences(num1):
    return num1.count(19) == 2 and num1.count(5) >= 3

print(check_occurrences([19, 19, 15, 5, 3, 5, 5, 2]))
print(check_occurrences([19, 15, 15, 5, 3, 3, 5, 2]))
print(check_occurrences([19, 19, 5, 5, 5, 5, 5]))
print("==================")

# 2. Write a Python program to find a list of integers containing exactly four distinct values, such that
# no integer repeats twice consecutively among the first twenty entries.The program should return
# True if conditions are met otherwise, it should return False.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

def check_distinct_values(num1):
    if len(set(num1)) != 4:
        return False
    num_range = 20
    if len(num1) <= 20:
        num_range = len(num1)
    for i in range(num_range - 1):
        if num1[i] == num1[i + 1]:
            return False
    return True

print(check_distinct_values([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
print(check_distinct_values([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]))
print(check_distinct_values([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))
print("==================")

# 3.Check Palindromes in List
# Write a Python program to check whether the given strings are palindromes or not. Return
# True otherwise False.
# Input:
# ['palindrome', 'madamimadam', '', 'four’', 'eyes']
# Output:
# [False, True, True, False, False]

def check_palindromes(str_list):
    return [s == s[::-1] for s in str_list]

str_list = ['palindrome', 'madamimadam', '', 'four', 'eyes', 'malayalam']
print(check_palindromes(str_list))
print("==================")

print("")
print("*#*#*++++++++++++++++++++++++++++++++++*#*#*")
print("")

# 19 Dec 2024 Homework
# 1. Write a Python program to count how many times the letter "a" appears in a given string.
# str1 = input("Enter a string : ")
str1 = "malayalam"
print(f"Number of 'a' in string : {str1} =", sum([1 for char in str1 if char == 'a']))
print("==================")

# 2. Write a Python function that takes a list of integers and returns a new list containing only the even numbers.
num_lst = [1, 2, 3, 4, 5, 6]
print([num for num in num_lst if num % 2 == 0])
print("==================")

# 3. Write a Python program to find the largest number in a list.
num_lst = [55, 32, 1, 328, 16, 15]
print(max([num for num in num_lst]))
print("==================")

# 4. Write a Python function that takes a dictionary where keys are
# names and values are ages. Return a list of names of people who
# are 18 years or older.
input_people = {'Alice': 17, 'Bob': 18, 'Charlie': 20, 'David': 15}
print([name for name, age in input_people.items() if age >= 18])
print("==================")