# Find the Second Largest Element Write a program to
# find the second-largest number in the list [10, 20, 4, 45, 99].

lst1 = [10, 20, 392, 4, 45, 45, 97, 99, 392]
print(lst1)
first_max = 0
second_max = 0
# method 1 :
for i in lst1:
    if i > first_max:
        first_max = i
lst1.remove(first_max)
for i in lst1:
    if second_max < i != first_max:
        second_max = i
print(second_max)
print("==================")

# method 2 :
lst1 = [10, 20, 392, 4, 45, 45, 97, 99, 392]
lst2 = []
len1 = len(lst1)
for i in range(2):
    largest_in_lst = 0
    for i in lst1:
        if i > largest_in_lst:
            largest_in_lst = i
    lst2.append(largest_in_lst)
    lst1.remove(largest_in_lst)
print(lst2)
print(largest_in_lst)
print("==================")

# method 3 :
lst1 = [10, 20, 392, 4, 45, 45, 97, 99, 392]
sorted_lst = []
largest_in_lst = 0
while True:
    largest_in_lst = max(lst1)
    sorted_lst.append(largest_in_lst)
    lst1.remove(largest_in_lst)
    if len(lst1) == 0:
        break
print(sorted_lst)
print("==================")

# method 4 :
# lst1 = [10, 20, 4, 45, 99]
lst1 = [10, 20, 392, 4, 45, 45, 97, 99, 392]
# largest_num = float("-inf")
# second_largest_num = float("-inf")
largest_num = -1*10**100
second_largest_num = -1*10**100
for i in lst1:
    if i > largest_num:
        second_largest_num = largest_num
        largest_num = i
    elif i > second_largest_num and i != largest_num:
        second_largest_num = i
print(second_largest_num)
