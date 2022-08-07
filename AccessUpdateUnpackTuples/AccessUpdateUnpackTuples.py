a=(10,20,30.4,"moni",10.32)
print("      Accessing the Elements of tuple    ")
print(a[0])
print(a[1])
print(a[3])
print()
print("      Update or Modifying the tuples    ")
# Tuples are Immutable, unchangeable but we can modify the tuples by workaround(by changing tuple into list then list into tuple)
print()
x=list(a)
x[3]="Mudasir"
x[0]=100
a=tuple(x)
print(a)
print()
print("      Unpack the tuples                ")# To Unpack tuples means that we can create variables equal to the numbers of elements of given tuple
# And access the elements by their just creating variables   
print()
(p,q,r,s,t)=a
print(p,q,r,s,t)
(p,q,*r)=a
print(p)
print(q)
print(*r)
""" Elements can't be add or removed from the touple when touple is created by it can be with the help of 
workaround(touple changing into list and then list changing into touple """
print()
print ("     Adding Element into the touple ")
print()
a=("apple","banana","cherry")
print("Oringal Elements are : ",a)
y=list(a)
y.append("Mango")
a=tuple(y)
print("After adding elements : ",a)
print()
print("    We can also remove the elements ") # By the same procedure 
print()
y=list(a)
y.remove("cherry")
a=tuple(y)
print(a)


