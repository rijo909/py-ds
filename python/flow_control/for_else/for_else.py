lst = [3, 5, 7, 9, 11, 12]
for i in lst:
    if i % 2 == 0:
        print("At least one even number found")
        break
else:
    print("No even number found")
