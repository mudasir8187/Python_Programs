x = ["apple", "banana", "cherry"]
print("    Removing Item by its name         ")
print("                                      ")
x.remove("apple")
print(x)
print("                                      ")
print("    Removing Item by it Index (Pop function)        ")
print("                                      ")
x.pop(1)
print(x)
print("                                      ")
print("   Removing item by delete function     ")
print("                                      ")
# If we use delete function it will delete the complete list rather if we specify the idex with it then it will delete the specific item
x = ["apple", "banana", "cherry"]
del x[2]
print(x)
print("                                      ")
print("    Clear Function ")
print("                                      ")
#The clear() method empties the list.
#The list still remains, but it has no content.
x = ["apple", "banana", "cherry"]
x.clear()
print(x)
