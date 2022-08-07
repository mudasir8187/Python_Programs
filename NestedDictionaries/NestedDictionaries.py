print("     Nested Dictionaries      ")
print()
a={1:{"name":"Moni","year":2001}, 2:{"name":"Ali","year":2000},3:{"name":"Mudasir","year":2001}}
print("     Accessing the Elements   ")
print()
print(a[1]['name'])
print(a[2]['year'])
print(a[3]['name'])
print()
print("     Adding a new element & dict into existing Dict")
print()
a[1]["age"]=21
print(a)
print()
a[2][1]={"E":2,"O":1}
print(a)
print()
# If we want to add an other dictonary 
a[4]={"name":'Rehman','year':1999}
print(a)
print()