import re
with open("regular_expression.txt", "r") as obj1:
    var1 = obj1.read()
patter_email = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.com')
print(patter_email.findall(var1))

patter_phone = re.compile(r'[0-9]+-[0-9]+-[0-9]+')
print(patter_phone.findall(var1))

patter_name = re.compile(r'\n\n([a-zA-Z ]+)\n')
print(patter_name.findall(var1))

patter_pincode = re.compile(r'[A-Z]{2} [0-9]+')
print(patter_pincode.findall(var1))

patter_town = re.compile(r'\, ([A-Z][a-z]+) [A-Z]{2}')
print(patter_town.findall(var1))
