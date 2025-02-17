# Create a dictionary where the keys are numbers from 1 to 20,
# and the values are the squares of those numbers.
from itertools import count

# Print all keys and their corresponding values.
# 2. Extract all keys where the square is greater than 150.
# 3. Find the sum of all squared values in the dictionary.
result_dict = {}
for i in range(1, 21):
    result_dict.update({i: i ** 2})
    # result_dict[i] = {}
    # result_dict[i]['number'] = i
    # result_dict[i]['square'] = (i)**2
print(result_dict)

lst1=[]
for i,j in result_dict.items():
    if j > 150:
        lst1.append(i)
print(lst1)

dict1_sum = 0
for i,j in result_dict.items():
    dict1_sum+=j
print(f'Sum is {dict1_sum}')

sentence = input("enter a sentence for count : ")
# sentence = "HelLo world!"
c1 = 0
dict1 = {}
for i in sentence.lower():
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)