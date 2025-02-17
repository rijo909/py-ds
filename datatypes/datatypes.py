# Numeric
var1 = 1 # Integer
print(type(var1), var1)
var2 = 3.14 # Float
print(type(var2), var2)
var3 = 3+1j # Complex
print(type(var3), var3)

# Boolean
var4 = True # Boolean
print(type(var4), var4)
var5 = False # Boolean
print(type(var5), var5)

# Sequence
var6 = "Hello World" # String
print(type(var6), var6)
var7 = 'Hi Good Morning' # String
print(type(var7), var7)
var8 = ["hello", 1.0, True, 10] # List
print(type(var8), var8)
var9 = ("hello", 1.0, True, 10) # Tuple
print(type(var9), var9)
var10 = range(2, 104, 4) # Range
print(type(var10), list(var10))
var11 = range(2, 5) # Range without step (default 1)
print(type(var11), list(var11))

# Sets
var12 = {1, 2, "Hello", 3.0, (5,6,7), tuple(range(8,20))}
print(type(var12), var12)

# Dictionary
var13 = {"name":"David", "age": 14, "Marks":85.3}
print(type(var13), var13)
