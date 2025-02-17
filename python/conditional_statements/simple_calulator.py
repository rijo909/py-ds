# Make asimple calculator application, it should perform basic arithemetic functions
# program should ask for 2 numbers
# program should ask type of operation (+, _, *, /)
# shold handle division by zero error with appropriate message

a = int(input("Please enter first number : "))
b = int(input("Please enter second number : "))
print("Choose an arithemetic operation fom the list \n"
  "1. Addition (Enter '1' or '+' for addition) \n"
  "2. Subtraction (Enter '2' or '-' for addition) \n"
  "3. Multiplication (Enter '3' or '*' for addition) \n"
  "4. Division (Enter '4' or '/' for addition) \n")
c=input("Please enter your arithemetic operator from above choices : ")
if c=='+' or c=='1':
    d = a+b
    print(a, '+', b,' = ',d)
elif c == '-' or c == '2':
    d = a - b
    print(a, '-', b, ' = ', d)
elif c == '*' or c == '3':
    d = a * b
    print(a, '*', b, ' = ', d)
elif c == '/' or c == '4':
    if b==0:
        print("division by zero is not possible")
    else:
        d = a / b
        print(a, '/', b, ' = ', d)
else:
    print("invalid operation entered")