# Nested list 
a= [10,20,30,40,[50,60]]
# [0]=10,[1]=20,[2]=30,[3]=40,[4]=[50,60]
# If we want to acces only the elements of index 4 then we call it by refrencing the index 4
# a[4][0]=50,a[4][1]=60
print(a)

print ("      Acessing Elements     ")
print()
print(a[3])
print(a[4][0])
print(a[4][1])
print()
print("      Modifying the elements ")
print()
a[1]=100
print(a)
a[4][1]=80
print(a)

# Some other types of nested list are following 
print("     Lists holds two or more lists  ")
print()
x=[[10,20,30],[40,50,60]]
print("     Accessing the Elements      ")
print()
print(x[0][0])
print(x[0][2])
print(x[1][2])
print()
print("     Modifying the Elements      ")
print()
x[0][1]=2
x[1][1]=5
print(x)