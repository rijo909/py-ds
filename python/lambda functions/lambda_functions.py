# lambda functions
# Anonymous functions
# Any arguments but one expression
# also called as inline functions, because we can define it and use immediately without defining it explicitly
# commonly used where simple functions are needed

# var1 = lambda x,y:x**2+y**2
# print(var1(10, 20))

# var1 = lambda x:x.isupper()
# print(var1(input("Enter a string : "))) # inputs can be used

# lambda function to add 10 to a given number
# var1 = lambda x:x+10
# print(var1(int(input("Enter a number : "))))

# square root of a given number
# var1 = lambda x:x**0.5
# print(var1(int(input("Enter a number : "))))

# Check if given number Starts with "A"
# var1 = lambda x:str(x).startswith("A")
# print(var1(input("Enter a string : ")))

# Lambda function to reverse a string
# var1 = lambda x:x[::-1]
# print(var1(input("Enter a string : ")))

# if else in lambda
# pos_neg = lambda a:"positive" if a>0 else ("zero" if a == 0 else "negative")
# print(pos_neg(int(input("Enter a number : "))))

# maximum number of 3 given values
# max_of_3 =lambda a,b,c: a if a>b and a>c else (b if b>a and b>c else c)
# print(max_of_3(1,2,2))

var1 = lambda x:True if len(x)>=5 else False
print(var1(input("Enter a string : ")))
