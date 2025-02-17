# Ask the user to enter a number between 10 and 20.
# If they enter a value under 10, display the message "Too low" and ask them to try again.
# If they enter a value above 20, display the message Too high" and ask them to try again.
# Keep repeating this until they enter a value that is between 10 and 20
# and then display the message "Thank you".

while_flag = True
while while_flag:
    num1 = float(input('Enter a number : '))
    if num1 < 10:
        print("Too low, try again")
    elif num1 > 20:
        print("Too high, try again")
    elif 10 <= num1 <= 20:
        print("Thank you")
        while_flag = False
    else:
        print("Wrong Input")