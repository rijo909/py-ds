# list
lst=[1, 4, 21, 32, 'hello', [1, 2, 3]] # heterogeneous with inner list
print(lst[-1]) # last index element
print(lst[2::-1]) # slicing
print(len(lst)) # length / count
lst[-1][1]=20 # inner list is accessed
print(lst)

# append - add value to last value of the list
lst.append(5); print(lst)

lst1 = []
for i in range(10):
    lst1.append(i+1)
print(lst1)

lst2 = []
for i in range(101):
    if i%3 == 0 and i%7 == 0:
        lst2.append(i)
print(lst2)

# pop - removes index or last element
lst = [1, 2, 3, 4, 6]
lst.pop(-1) # removes last element
lst.pop() # removes last element
print(lst)

# remove - removes the data from the list
lst = [1, 2, 3, 4, 5, 6, 5]
lst.remove(5) # removes first occurrence of the data
print(lst)

# insert
lst = [1, 2, 3, 4, 5, 6]
lst.insert(-1, 7) # inserts to second last position of the list
print(lst)
lst.insert(200, 7) # inserts to the very last position of the list
# if index is greater than the maximum index possible it moves to last element

# index
lst = [1, 2, 3, 4, 5, 6, 4, 4]
print(lst.index(4)) # first occurrence of the data is returned, if no data it shows error

# count
lst = [1, 4, 2, 4, 3, 4, 5, 6, 4, 4]
print(lst.count(4)) # number of occurrence of the data, returns zero if no data is found in list

# extend
lst = [1, 2, 3]
lst.extend([4,5,6])
print(lst)

# concatenation
lst1 = [1, 2]
lst2 = [3,4]
lst1.extend(lst2)
print(lst1)

# reverse
lst1 = [1, 2, 3, 4, 5, 6]
lst1.reverse()
print(lst1)

# sort
lst1 = [7, 2, 9, 3, 5, 4, 1]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

# def lstEven(q):
#     if q % 2 == 0:
#         return q
# lst1.sort(reverse=False, key=lstEven)
# print(lst1)

# sorted
lst=[3,5,1,7,4,4,9]
print(sorted(lst)) # it's a function that can be done on different datatypes, not just list
print(sorted(lst, reverse=True))
print(sorted("AB#cH.eL1"))

# copy
lst = [1 , 2, 3]
lst1 = lst.copy()
lst1.append("hello")
print(lst)
print(lst1)