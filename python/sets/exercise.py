# Create a set: fruits = {"apple", "banana" "cherry"}.
# • Add "orange" to the set.
# • Remove "banana" from the set.
# • Discard "grape" from the set (no error should occur if it's not present).
# • Print the final set

fruit_set = {"apple", "banana", "cherry"}
fruit_set.add("orange")
print(fruit_set, "\n")

fruit_set.remove("banana")
print(fruit_set, "\n")

fruit_set.discard("grape")
print(fruit_set, "\n")

# update with multiple items "kiwi", "strawberry", "pineapple"
fruit_set.update(("kiwi", "strawberry", "pineapple"))
print(fruit_set, "\n")
