# write a program to check if a given number is prime or not
# num1=int(input("Enter a number to check if prime : "))
# c=0
# for i in range(1, num1+1):
#     if num1%i == 0:
#         c+=1
# if c==2:
#     print("Number is prime")
# else:
#     print("Number is not prime")

num1=int(input("Enter a range to get prime numbers : "))
p_limit = 20
for i in range(1, num1+1):
    c=0
    c1=0
    for j in range(2, i//2):
        if i%j == 0:
            c+=1
    if c==0 and i != 1:
        c1+=1
        if c1==p_limit:
            print(i, end="\n")
            c1=0
        else:
            print(i, end=", ")