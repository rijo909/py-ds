# 1. Check if a String Starts with a Vowel
# Write a program to check if a given string starts with a vowel.
# Input:
# "Apple"
# "Banana"
#
# Expected Output:
# Apple starts with a vowel.
# Banana does not start with a vowel.
#
# Hint: Use startswith() and a tuple of vowels: ("a", "e", "i", "o", "u").

# =============Answer=============
# user_word = input("Please enter your word : ")
# if user_word.lower().startswith(("a", "e", "i", "o", "u")):
#     print(user_word, "starts with a vowel")
# else:
#     print(user_word, "does not start with a vowel")

# 2. Case Conversion
# Write a program that converts a given string to uppercase if it is lowercase, or to lowercase if it is uppercase.
# Input:
# "hello"
# "WORLD"
#
# Expected Output:
# HELLO
# world
#
# Hint: Use isupper(), islower(), upper(), and lower().

# =============Answer=============
# user_word = input("Please enter your word : ")
# if (user_word.islower()):
#     print(user_word, "is lower case")
#     print(user_word.upper())
# elif (user_word.isupper()):
#     print(user_word, "is upper case")
#     print(user_word.upper())
# elif (user_word.isnumeric()):
#     print(user_word, "is numeric")
# else:
#     print(user_word, "is both lowwercase and uppercase")

# 3. Check if a String Contains Only Digits
# Write a program to check if a given string contains only digits.
# Input:
# "12345"
# "hello123"
#
# Expected Output:
# 12345 contains only digits.
# hello123 does not contain only digits.
#
# Hint: Use isdigit().

# =============Answer=============
# user_word = input("Please enter your word : ")
# if user_word.isnumeric():
#     print(user_word, "contains only digits")
# else:
#     print(user_word, "does not contain only digits")

# 4. String Length and Condition
# Write a program to check if the length of a string is greater than 5.
#
# Input:
# "hello"
# "welcome"
#
# Expected Output:
# hello has 5 or fewer characters.
# welcome has more than 5 characters.
#
# Hint: Use len() and conditional statements.

# =============Answer=============
# user_word = input("Please enter your word : ")
# if len(user_word) > 5:
#     print(user_word, "has more than 5 characters")
# elif len(user_word) <= 5:
#     print(user_word, "5 or fewer characters.")
