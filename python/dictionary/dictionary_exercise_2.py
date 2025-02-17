str1 = "the that this here that the the those this here"
dict1 = {}
lst1 = str1.split()
print(lst1)
for i in lst1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

for i,j in dict1.items():
    print(i, j)