lst1 = ["1", 2, "hello"]
lst2 = ["DFA", "a", "b"]
dict1 = {1:lst1, 2:lst2}
import pickle
with open("demo.pkl", "wb") as obj1: # write binary
    pickle.dump(dict1, obj1) # write mode is .dump argument and file object
with open("demo.pkl", "rb") as obj1: # read binary
    var1 = pickle.load(obj1) # rea mode is .load and file object
print(var1)