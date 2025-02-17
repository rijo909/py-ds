import random

# Randomly choose either heads or tails ("h" or "t").
# Ask the user to make their choice.
# If their choice is the same as the randomly selected value,
# display the message "You win", otherwise display "Bad luck".
# At the end, tell the user if the computer selected heads or tails.

while True:
    lst = ["h", "t"]
    var1 = input("Please enter your choice (h or t) : ")
    if var1.lower() in lst:
        # var2 = random.randint(1,2)
        var2 = random.choice(lst)
        print(f"computer chosen answer is : {var2}")
        # if (var2 == 1 and var1 == "h") or (var2 == 2 and var1 == "t"):
        if var1 == var2:
            print("You win")
            break
        else:
            print("Bad luck")
            break