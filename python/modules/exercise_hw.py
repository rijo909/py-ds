import  random
# Randomly choose a number between 1 and 25.
# Ask the user to pick a number. If they guess correctly, 
# display the message "Well done" otherwise tell them if they are too high 
# or too low and ask them to pick a second number. 
# If they guess correctly on their second guess, 
# display "Correct", otherwise display "You lose"

# int1 = random.choice(range(1,26))
# print(f"computer chosen value : {int1}")
# while True:
#     int2 = int(input("Enter a number from 1 to 25 : "))
#     if int2 == int1:
#         print("Well done!")
#         break
#     elif int1-5 > int2:
#         print("too low")
#     elif int1 > int2:
#         print("low")
#     elif int1+5 < int2:
#         print("too High")
#     elif int1 < int2+5:
#         print("High")
#     else:
#         print("wrong input...")

int1 = random.choice(range(1,26))
print(f"computer chosen value : {int1}")
try_count = 0
while True:
    if try_count == 0:
        int2 = int(input("Enter a number from 1 to 25 : "))
    else:
        int2 = int(input("Enter a number again from 1 to 25 : "))
    if int2 == int1:
        if try_count == 0:
            print("You guessed correctly, well done!")
            break
        else:
            print("You guessed correct")
            break
    elif int1 > int2:
        if try_count == 0:
            print("too low")
        else:
            print("too low, You lose")
            break
    elif int1 < int2:
        if try_count == 0:
            print("too High")
        else:
            print("too High, You lose")
            break
    try_count+=1