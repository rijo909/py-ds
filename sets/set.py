set1 = {True, 1, False, 0}
print(set1) # only 2
print("count : ", len(set1), "\n") # only 2

# add
set1.add((1,2,3)) # adds as one element of the tuple block
print(set1)
print("count : ", len(set1), "\n")

set1.add("hello") # add possible
print(set1)
print("count : ", len(set1), "\n")

# update
set1.update([1,2,3,4])
print(set1)
print("count : ", len(set1), "\n")

set1.update("hello")
print(set1)
print("count : ", len(set1), "\n")

# remove
set1.remove('hello')
print(set1)

# discard
set1.discard(10) # won't show an error if its not there in the set (can be used for checking)
set1.discard('h')
print(set1)
print("count : ", len(set1), "\n")

# clear
set2 = {1, 0}
set3 = set2.copy() # copies the original set to the next without dependencies (storage location not same here)
set3.clear()
print(set2, "\n")