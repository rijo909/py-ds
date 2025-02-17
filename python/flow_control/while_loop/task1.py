# ask user to enter number until he enters a value over 5
# if over 5 print the last number entered is [number] and stop program

num1=True
while num1:
    user_num = int(input("Enter a number : "))
    if user_num > 5:
        print("Last number entered is ", user_num)
        num1=False