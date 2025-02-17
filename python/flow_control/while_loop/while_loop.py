# multiples of 3 and 9 and count how many
n=1000
c=0
i=1
while i<=n:
    if i%3 == 0 and i%9 == 0:
        c+=1
        if c%25==0:
            print(i, end=" \n")
        else:
            print(i, end=", ")
    i+=1
print("\n\nNumber of multiples : ", c)
