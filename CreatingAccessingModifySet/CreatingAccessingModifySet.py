a={10,20,30.4,"moni",80.32}
# Sets are immutable,unchangeable unordered not index
print("      Accessing the Elements of sets  ")
print()
print("We can't access and changed  the Elements because the elements are unordered and not indexed ")
print()
print("      Adding  Elements    ")
print()
# With the help of add() we can add element
a.add("Mudasir")
print(a)
# we can also add list,tuple,dictionaryinto the set by using update function 
b=["Ali","Looking Good"]
a.update(b)
print(a)
print()
print("      Removing Elements   ")
print()
# With the help of remove() we can remove  element
a.remove(10)
print(a)
# we can also use pop() but by by this function we don't know which element will be eliminated
a.pop()
print(a)