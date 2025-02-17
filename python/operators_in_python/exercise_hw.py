# num1=int(input("Enter a number : "))
# if num1==0:
#     print("The number is zero")
# elif num1>0:
#     print("The number is positive")
#     if num1<10:
#         print("The number is small")
#     elif num1>10 and num1<100:
#         print("The number is medium")
#     elif num1>100:
#         print("The number is large")
# elif num1<0:
#     print("The number is negative")

num1=int(input("Enter age : "))
if num1>=0 and num1<=12:
    print("child")
elif num1>=13 and num1<=17:
    print("teenager")
elif num1>=18 and num1<=64:
    print("Adult")
    if num1>=18 and num1<=35:
        print("young adults")
    if num1 >= 36 and num1 <= 64:
        print("middle aged")
elif num1>=65:
    print("Senior")