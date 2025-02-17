a=int(input("Enter a number : "))
if a%3==0 and a%7==0:
    print(a, " is multiple of 3 and 7")
if a%3==0 and a%7!=0:
    print(a, " is multiple of 3 but not multiple of 7")
if a%3!=0 and a%7==0:
    print(a, " is not multiple of 3 but a multiple of 7")
else:
    print(a, " is not multiple of 3 and 7")