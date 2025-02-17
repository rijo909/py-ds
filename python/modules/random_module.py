import random

# randint - random integer
var1 = random.randint(1,100)
print(var1)

var2 = random.randint(1,2)
if var2 == 1:
    print("Head")
else:
    print("Tail")

lst1 = ["David", "Malavika", "Amal Raj", "Priya"]
# random - choice
print(random.choice(lst1))

# shuffle list
random.shuffle(lst1)
print(lst1)
