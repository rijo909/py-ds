# # Method 1
# n=input("enter the number : ")
# sum1=0
# for i in n:
#     sum1+=int(i)
# print(sum1)

# Method 2
n=int(input("enter the number : "))
num1=n
sum1=0
for i in range(len(str(num1))):
    d=num1%10
    sum1+=d
    num1//=10
print(sum1)