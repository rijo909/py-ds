with open("sample1.txt", "w") as obj1:
    # obj1.read() # not possible
    # obj1.write(10) # write arg must be string
    # obj1.write("10")
    # for i in range(1, 1001):
    #     obj1.writelines(["a\n", "b\n", "c\n"])
    #     obj1.write(f"{i}\n")
    obj1.write("python")
    obj1.seek(0, 0)
    obj1.write("hello")