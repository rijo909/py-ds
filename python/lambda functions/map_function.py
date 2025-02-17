str1 = ["hello", "34", "python", "Java", "Programming"]
lst=list(filter(lambda a:a[0].isupper(), str1)) # starts with capital letter
print(lst)
lst=list(filter(lambda a:a.isdigit(), str1)) # returns only numbers
print(lst)
lst=list(filter(lambda a:len(a)>=5, str1)) # strings greater than equal to 5
print(lst)
