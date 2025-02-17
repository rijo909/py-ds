# Create a dictionary with the following key-value pairs: {"Name": "John", "Age": 25, "City": "New York"}.
# o Access the value of the key "Age".
# O Update "City" to "Los Angeles".
# o Add a new key "Country" with the value "USA".
# o Delete the key "Age".
# Check if the key "Name" exists in a dictionary.
# If it exists, print its value; otherwise, print "Key not found",

dict1 = {"Name": "John", "Age": 25, "City": "New York"}
print(dict1)
print(dict1["Age"])
dict1["City"] = "Los Angeles"
print(dict1)
dict1["Country"] = "USA"
print(dict1)
del dict1["Age"]
print(dict1)
if 'Name' in dict1:
    print(dict1['Name'])
else:
    print("Key not found")
