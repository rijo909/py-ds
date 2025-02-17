from functools import reduce

lst = [1, 2, 3, 4, 5]
var1 = reduce(lambda a, b: a**1 + b**2, lst)
print(var1)

lst = [2, 2, 3, 4, 5]
var1 = reduce(lambda a, b: a + b**2, lst, 0) # starts with a=0, and not with the list,
# hence correct result
print(var1)

lst = [4, 2, 3, 4, 5]
var1 = reduce(lambda a, b: a + b**2, lst, 0)
print(var1)

# longest string in list
lst=['cat', 'elephant', 'hippopotamus1', 'dog', 'hippopotamus']
var1 = reduce(lambda a,b: b if len(a) < len(b) else a, lst)
print(var1)

