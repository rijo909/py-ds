# dictionaries are mutable
# keys need to be immutable
# keys need to be unique
# represented by curly brackets
# key-value pairs
# ordered
# iterable
# mutable
# no indexing
# heterogeneous values can be added
# value can be duplicate

dict1 = {} # initialising a dictionary
dict1 = {1:'vishak', 20:'anson', 2:'malavika'}
print(dict1)

print()
dict1 = {1:'apple', 2:'banana',3:'orange', 4:'grape', 5:'butter_fruit'}
print(dict1)
print(len(dict1))

# index
print()
print('key 4 value =', dict1[4])

# update - multiple values using another key, value pair dictionary
print()
dict1[4] = "Rinkle"
print(dict1)

# add - key:value pair to dictionary
print()
dict1[6]='grape'
print(dict1)

dict1={1:{1:2, 3:{4:"hello"}}}
print()
print(dict1)
print(dict1[1][3][4])
