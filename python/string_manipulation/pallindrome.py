str1 = input("Enter a word : ")
str1 = str1.lower()
reverse_str1 = str1[::-1]
if str1 == reverse_str1:
    print("it is palindrome")
else:
    print("it is not palindrome")