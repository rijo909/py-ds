tup = (1, 2, 3, 4, 5)

# index
print(tup.index(2))

# count
print(tup.count(3))

# slicing
print(tup[::-1])
print(tup[-1])

# sorted function
print(sorted(tup)) # sorted list output
print(sorted(tup, reverse=True)) # reverse list output
print(sorted(tup)[-2]) # second largest list output

# sum
print(sum(tup)) # sum of elements

# min
print(min(tup)) # minimum of elements

# max
print(max(tup)) # maximum of elements

print(sum(tup)/len(tup)) # prints average of elements

