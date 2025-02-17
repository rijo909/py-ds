import random

# Randomly pick a whole number between 1-and 10.
# Ask the user to enter a number and keep entering numbers until they
# enter the number that was randomly picked.

# int1 = random.choice(range(1,11))
int1 = random.randint(1, 10)
# print(f"computer chosen value : {int1}")
while True:
    int2 = int(input("Enter a number from 1 to 10 : "))
    if int2 == int1:
        print("You correct guessed!")
        break
    else:
        print("wrong...")
