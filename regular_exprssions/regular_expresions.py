import re
var1 = """Name: Afsana
Pincode : 680028 h
Phone: 1203838022"""
phone = re.compile(r'Pincode : (\d{6})')
name = re.compile(r'Name : ([a-zA-z])')
res = phone.findall(var1)
res_name = name.findall(var1)
print(res)
print(res_name)

var2 = "rijo@test.com Anand 1223344 marcus@play.biz 11445522"
usr_emails = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com')
user_a = re.compile(r'([aA]\w{4}) ')
print(usr_emails.findall(var2))
print(user_a.findall(var2))
var3 = "rijo@test.com Anand 1223344 marcus@play.biz 11445522"
print(re.sub(r'\s', '-', var3))
print(re.sub(r'[0-9]+', '***', var3))
var3 = "rijo@test.com Anand 1223344 marcus@play.biz 11445522"
text1 = 'anad and Arun are A Friends'
pattern = re.compile(r'\b[A-Z][a-z]*\b')
print(pattern.findall(text1))