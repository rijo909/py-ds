# a=int(input("Enter a number : "))
# if a%2!=0:
#     print("Number is Odd")
# elif a==0:
#     print("Number is Zero")
# else:
#     print("Number is Even")

# a=int(input("Enter a number : "))
# if a%7==0:
#     print("Number is divisible by 7")
# else:
#     print("Number is not divisible by 7")

# a=int(input("Enter a number : "))
# if a==0:
#     print("Number is zero")
# elif a%5==0:
#     print("Hello!")
# else:
#     print("Bye!")

# a = int(input("Enter a number : "))
# if a == 0:
#     print("Number is zero")
# else:
#     a = a % 10
#     if a%3 == 0:
#         print("last digit is divisible by 3")
#     else:
#         print("last digit is not divisible by 3")

# a = int(input("Enter a your age : "))
# if a == 0:
#     print("Age can't be zero")
# else:
#     if a>=18:
#         print("You are eligible to vote")
#     else:
#         print("You are not eligible to vote")

a = int(input("Please enter you marks in percentage : "))
if a == 0:
    print("Mark can't be zero")
else:
    if a>90 and a<=100:
        print("You are awarded A grade")
    elif a>80 and a<=90:
        print("You are awarded B grade")
    elif a>60 and a<=80:
        print("You are awarded C grade")
    elif a<60 and a>=0:
        print("You are awarded D grade")
    else:
        print("Mark entered is invalid")