with open("sample.txt", "r") as obj1:
    # var1 = obj1.read()
    # var2 = obj1.readlines()
    # var3 = obj1.readline()
    print(obj1.tell()) # provides cursor position
    print(obj1.seek(0, 0)) # moves cursor to specific position in first param and second param is mode
    # print(var1)
    # print(var2)
    # print(var3)
# obj1.read() # file object can be used outside block