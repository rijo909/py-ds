# str1 = ("heLlo j2344dGd059jf")
# # str2 = ("world")
# upper_c = lower_c = digit_c = 0
# for i in str1: # i =
#     if i.isdigit():
#         digit_c+=1
#     if i.islower():
#         lower_c+=1
#     if i.isupper():
#         upper_c+=1
# # print(str2)
# print("digit count : ", digit_c)
# print("upper count : ", upper_c)
# print("lower count : ", lower_c)

# lower_limit = 0
# upper_limit = 100
# c_even = 0
# c_odd = 0
# c_mul_3_and_7 = 0
# for i in range(lower_limit, upper_limit+1):
#     # print(i, end=" ")
#     if i==0:
#         print('===============================')
#     else:
#         if i%2 == 0:
#             c_even+=1
#         else:
#             c_odd+=1
#         if i%3 == 0 and i%7==0:
#             c_mul_3_and_7+=1
# print("odd count : ", c_odd)
# print("even count : ", c_even)
# print("multiple of 3 and 7 count : ", c_mul_3_and_7)

# u_name = input("Enter the name : ")
# u_name_c = int(input("Enter the how many times you want it displayed : "))
# for i in range(0, u_name_c):
#     print(u_name, end=" ** ")
# print("\n================================\n")
# for i in u_name:
#     print(i)

# number_table_val = int(input("Enter the number for the multiplication table between 1 and 12: "))
# if number_table_val>= 1 and number_table_val <= 12:
#     number_table_val_limit = int(input("enter the limit : "))
#     for i in range(0, number_table_val_limit+1):
#         print(i, " x ", number_table_val,  " = ", i*number_table_val)
# else:
#     print("Number entered is not between 1 and 12")

# u_name = input("Enter the name : ")
# u_name_c = int(input("Enter the how many times you want it displayed : "))
# if u_name_c >= 0 and u_name_c > 10:
#     # for i in range(3):
#     #     print("Too High")
#     print("too High \n"*3)
# else:
#     for i in range(u_name_c):
#         print(u_name)

# armstrong number
# num1 = int(input("Enter a number : "))
# # 1**3+5**3+3**3 = 153
# str1 = str(num1)
# digits_count = len(str1)
# c=0
# for i in str1:
#     c+=int(i)**digits_count
# if c==num1:
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

# # find all armstrong numbers within a limit : print them comma seperated
# limit = int(input("Enter a limit : "))
# armstrong_numbers = []
# for j in range(0, limit+1):
#     str1 = str(j)
#     digits_count = len(str1)
#     c=0
#     for i in str1:
#         c+=int(i)**digits_count
#     if c==j:
#         print(j, end=",")

# # find sum of 30 natural numbers
# limit = int(input("Enter a limit : "))
# sum=0
# for j in range(1, limit+1):
#     sum+=j
# print(sum)

# # Ask how many people the user wants to invite to a party.
# # If they enter a number below 10, ask for the names and
# # after each name display "[name] has been invited". If
# # they enter a number which is 10 or higher, display the
# # message "Too many people"
# limit = int(input("Enter how many people the you want to invite to a party : "))
# if limit <= 10:
#     for j in range(1, limit+1):
#         name = input("\nPlease enter name"+str(j)+": ")
#         print(name, "has been invited")
#     print("\n\nThanks!")
# else:
#     print("Too many people")

# # find factorial of a number
# num1 = int(input("Enter a limit : "))
# num_fact = 1
# for i in range(1, num1+1):
#     num_fact*=i
# print(num_fact)

# iterable datatypes : list, string, tuple, range, dictionary, set

# # number of vowels in a string
# var1 = input("Enter string to count vowels: ")
# vowels = "aeiou"
# c=0
# for i in var1:
#     if i.lower() in vowels:
#         c+=1
# print("Number of vowels in the string :", c)

## iterating through list

lst=[21, 90, 32, 12, 25, 12]
sum1=0
for i in lst:
    if i%2==0:
        sum1+=i
print(sum1)