# # Write a program to find the first number divisible by 7 and 4 in
# #  the range of 1 and 50, Note only need to print first appearing number
#
# for i in range(1,51):
#     if i%7 == 0 and i%4 == 0:
#         print(i)
#         break

# write a program to all numbers from 100 to 300
# except palindrome numbers

for i in range(100, 301):
    if str(i) == str(i)[::-1]:
        continue
    print(i, end=' ')
