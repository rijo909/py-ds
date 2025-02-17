from os.path import split

lst = []
for i in range(1, 101):
    lst.append(i)
# print(lst)

lst = [i for i in range(1, 101)] # concise way of taking the range instead of for loop
# print(lst)

lst = [i for i in range(1, 101) if len(str(i)) == 2] # condition applied to final list result
# print(lst)

# a  list of squares from 1 to 10
lst = [i**2 for i in range(1, 11)]
# print(lst)

# list of numbers divisible by 3 and 9 between 100 and 200
lst = [i for i in range(100, 201) if i%3==0 and i%9==0]
# print(lst)

# extract all characters that are not vowels
str1="List comprehension is powerful"
lst = list(set([i.lower() for i in str1 if i.lower() not in "aeiou"]))
# print(lst)

# list of word lengths
str1 = "The quick brown fox jumps over the lazy dog"
lst = [len(i) for i in str1.split()]
# print(lst)

# Reverse each word in the list ["Python", "is", "fun"]. Output: ['nohtyP', 'nuf']
lst1 = ["Python", "is", "fun"]
# lst2 = [i[::-1] for i in lst1 if len(i) > 2]
# print(lst2)

# Convert a list of temperatures in Fahrenheit [32, 68, 100, 212] to Celsius
# using the formula (F - 32) * 5/9. Output: [0.0, 20.0, 37.77777777777778, 100.0]
lst1 = [32, 68, 100, 212]
# lst2 = [(i - 32) * 5/9 for i in lst1]
# print(lst2)

set1 = {i for i in range(1, 101)} # set comprehension

dict1 = {i:i**2 for i in range(1,101)} # dictionary comprehension
# print(dict1)

# Flatten a 2D list into a 1D list using list comprehension
# Input : [[1,2][3,4][5,6]]
# Output : [1,2,3,4,5,6]
lst1 = [[1, 2], [3, 4], [5, 6]]
# lst2 = list()
# lst3 = list()
# lst2 = [list(enumerate(i)) for i in lst1]
# print(lst2)
# lst2 = [i.pop(0) for i in lst1]
# lst3 = [i.pop() for i in lst1]
# lst2.extend(lst3)
lst2=[j for i in lst1 for j in i]
print(lst2)

# replace negative numbers in a list with 0
num_list = [-1, 2, -3, 4, -5]
reslt_list = [0 if i<0 else i for i in num_list]
print(reslt_list)

# Extract Dictionary Keys Create a list of keys from a dictionary
# whose values are greater than a threshold.
# my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
# threshold = 10
# Output: ['b', 'd']
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
threshold = 10
# reslt_list = [i if j>10 else '' for i,j in my_dict.items()]
reslt_list = [i for i, j in my_dict.items() if j > threshold]
print(reslt_list)