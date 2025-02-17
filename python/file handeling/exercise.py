# # Write and Read a File
# # 1. Create a file named example. txt using write mode.
# with open("example.txt", "w") as obj1:
#     pass
# # 2. 2. Write the following lines into the file:  Python is an amazing programming language.
# # It is widely used in data science and web development.
# with open("example.txt", "w") as obj1:
#     obj1.write("Python is an amazing programming language.\nIt is widely used in data science and web development.")
#
# # 3. Close the file and open it again in read mode.
# # 4. Read and print the file content.
# with open("example.txt", "r") as obj2:
#     var1 = obj2.read()
#     print(var1)
#
# # Append and Read a File
# # 1. Open the file example. txt in append mode.
# # 2. Add the following line to the file: It also supports machine learning and AI.
# with open("example.txt", "a") as obj3:
#     obj3.write(" It also supports machine learning and AI")
# # 3. Close the file and reopen it in read mode.
# # 4. Print all the content of the file.
# with open("example.txt", "r") as obj4:
#     var1 = obj4.read()
#     print(var1)

# "C:\Users\rijok\Downloads\palindromes.txt"
with open(r"C:\Users\rijok\Downloads\palindromes.txt", "r+") as obj1:
    str_line = obj1.read().split()
    lst1 = list()
    for i in str_line:
        if i.lower() == i[::-1].lower():
            print(i)
