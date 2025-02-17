# Arithemetic Operators
from tkinter.constants import FALSE

a=230
b=21
print("Addition : ", a+b)
print("Subtraction : ", a-b)
print("Multiplication : ", a*b)
print("Division : ", a/b)
print("Floor : ", a//b)
print("Modulus : ", a%b)
print("Power : ", a**b)

print('============================')

# Comparison Operators
print("Equal to : ", a==b)
print("Greater than : ", a>b)
print("Greater than equal to : ", a>=b)
print("Less than : ", a<b)
print("Less than equal to : ", a<=b)
print("Not equal to : ", a!=b)

print('============================')

# Logical Operators
print("and ", True and True)
print("and ", True and False)
print("and ", False and True)
print("and ", False and False)

print("or ", True or True)
print("or ", True or False)
print("or ", False or True)
print("or ", False or False)

print("not ", not True)
print("not ", not False)

print('============================')

# Compound operators
a=30; b=10
a+=b
print("Addition : ", a)
a=30; b=10
a-=b
print("Subtraction : ", a)
a=30; b=10
a*=b
print("Multiplication : ", a)
a=30; b=10
a/=b
print("Division : ", a)
a=30; b=10
a//=b
print("Floor : ", a)
a=30; b=10
a%=b
print("Modulus : ", a)
a=30; b=10
a**=b
print("Power : ", a)

# Identity Operator
a=30; b=10
print(a is b)
a=2; b=2
print(a is b)
