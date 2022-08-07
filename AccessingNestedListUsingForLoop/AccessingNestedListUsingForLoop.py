a=[10,20,30,[40,50]]
x=len(a) # 1,2,3,4
for i in range (x):
    if type (a[i]) is list:
     if len(a[i])>0: # 0,1
      m=len(a[i])
      for j in range (m):
         print(i,j,a[3][j])
    else :
       print(i,a[i])
          
      
        