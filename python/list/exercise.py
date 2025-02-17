lst1=[1, 2, [2, 1, [2, 1, "hello"]], 2]
print(lst1)

#1. Change the value "hello" to "Hello world"
lst1[2][2][2] = "hello world"
print(lst1)

#2. Add an element "python" to the list,
# [2,1,"hello"] in its 2nd index.
lst1[2][2].append("python")
print(lst1)

#3. Remove the word "hello world" from the above-mentioned list.
if lst1[2][2][2].count("hello world") > 0 :
    lst1[2][2].remove("hello world")
print(lst1)

#4. Extend the main list lst1 with the values ("a", "b")
lst1.extend(("a", "b"))
print(lst1)

#5. Remove the last from the main list and return
# the value into a variable last_element
last_element = lst1.pop()
print(last_element)
