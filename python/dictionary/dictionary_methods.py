# pop - remove the key value pair from dictionary
dict1 = {"hello":"world",2:{1,2},3:{1:'hari',2:"abhi",3:{1:1}}}
print(dict1.pop("hello"))
print(dict1)

# print(dict1.pop()) # expects an index in pop
# print(dict1)

dict1 = {"hello":"world",2:{1,2},3:{1:'hari',2:"abhi",3:{1:1}}}
print(dict1[3].pop(1))
print(dict1)

# popitem - removes last pair and returns as comma separated tuple
dict1 = {"hello":"world",2:{1,2},3:{1:'hari',2:"abhi",3:{1:1}}}
print(dict1.popitem()) # key value pair coma separated; returned as tuple
print(dict1)

# dict1 = {"hello":"world",2:{1,2},3:{1:'hari',2:"abhi",3:{1:1}}}
# print(dict1.popitem(2)) # wont take any index
# print(dict1)

# update - add more than one key value pairs
dict1 = {}
dict1.update({1:"one", 2:"two"})
print(dict1)

# del
dict1 = {"hello":"world",2:{1,2},3:{1:'hari',2:"abhi",3:{1:1}}}
del dict1[2]
print(dict1)

# membership operator
if "hello" in dict1: # check "hello" is in keys
    print("is a key member")

if "world" in dict1.values(): # check "hello" is in keys
    print("is a value member")

# print all keys
print(dict1.keys())

# print all keys
print(dict1.values())

# clear
# copy
# del - remove an element
dict2 = dict1.copy()
dict1.clear()
print(dict1, dict2)
