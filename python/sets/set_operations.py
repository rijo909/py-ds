set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("set 1 : ", set1, "\n")
print("set 2 : ", set2, "\n")

# 1. union
set3 = set1.union(set2)
print("Union : ", set3, "\n")

# 2. intersection
set3 = set1.intersection(set2)
print("intersection : ", set3, "\n")

# 3. difference
set3 = set1.difference(set2)
print("difference set1 on set2 : ", set3, "\n")
set3 = set2.difference(set1)
print("difference set2 on set1 : ", set3, "\n")

# 4. symmetric difference - difference and the union of non common elements
set3 = set1.symmetric_difference(set2)
print("symmetric difference set1 on set2 : ", set3, "\n")

# 5. disjoint - if no common elements
set3 = set2.isdisjoint(set1)
print("is dis joint? : ", set3, "\n")

# 6. subset
set4 = {3, 4}
set5 = {1, 3, 4, 7, 10}
print("set4 : ", set4)
print("set5 : ", set5)

set3 = set4.issubset(set5)
print("set4 is sub set set5? : ", set3)
set3 = set5.issubset(set4)
print("set5 is sub set set4? : ", set3, "\n")

# 7. superset
print("set4 : ", set4)
print("set5 : ", set5)
set3 = set4.issuperset(set5)
print("set4 is super set set5? : ", set3)
set3 = set5.issuperset(set4)
print("set5 is super set set4? : ", set3, "\n")
