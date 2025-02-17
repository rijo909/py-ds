with open("sample1.txt", "a") as obj1:
    obj1.write("newer")
    obj1.seek(0, 0)
    obj1.write("text")