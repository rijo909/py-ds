lst1=["hello", "python", "programming", "java", "javascript"]

# show all words greater than 5
rsl_word_lst = []
rsl_word_count_lst = []
rsl_vowel_count_lst = []
for i in lst1:
    if len(i) > 5 :
        rsl_word_lst.append(i)
        rsl_word_count_lst.append(len(i))
print(rsl_word_lst)
print(rsl_word_count_lst)

# number of vowels in the list of strings
vowels = "aeiou"
for i in lst1:
    c=0
    for j in i:
        if j in vowels:
            c+=1
    rsl_vowel_count_lst.append(c)
print(rsl_vowel_count_lst)

# show all palindrome words in a list
rsl_palindrome_lst = []
lst_sample = ["malayalam", "hello", "nivin", "dad", "python", "Mom"]
for i in lst_sample:
    if i.lower() == i[::-1].lower():
        rsl_palindrome_lst.append(i.lower())
print(rsl_palindrome_lst)
