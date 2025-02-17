from curses.ascii import isupper, islower, isdigit, isalpha, isalnum

var1 = "  HeLlO  wOrLd  "
print(var1)

# Upper case
print(var1.upper())

# Lower case
print(var1.lower())

# Capitalise
print(var1.capitalize())

# Title
print(var1.title())

# Strip
var2=" #### Good Morning ## ## "
print(var2.strip("# "))
var2=" #### Good Morning ## ## "
print(var2.strip("G# o")) # start or end with the parameter values, not inbetween

# Replace
var2=" #### Good Morning ## ## "
print(var2.replace("# ","*"))
var2=" #### Good Morning ## ## "
print(var2.replace("#","").strip(" ").title()) # fully cleans the string from all noices

# Split
var1="Hello World  Good Morning "
print("var1.split(" ")")
print(var1.split(" "))
var1="Hello World  Good Morning "
print("var1.split('o')")
print(var1.split("o"))

# Length
var1="Hello World  Good Morning "
print(len(var1))
var2 = var1.split()
print(len(var2))

# isupper()
var3="HELLO"
print(isupper(var3))

# islower()
print(islower(var3))

# isdigit
print(isdigit(var3))

# isalpha
print(isalpha(var3))

# isalnum
print(isalnum(var3))

# startswith()
print(var3.startswith("H"))

# endswith()
print(var3.endswith("O"))
