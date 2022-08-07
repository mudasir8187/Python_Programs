"""class Car():
    def __init__(self):
        self.name="Toyata"
        self.model="Yars"
        self.year=2021
    def show(self):
         print("Car Name is:",self.name,"and the model is:",self.model,"and the year is:",self.year)
mycar=Car()     
mycar.show()"""

class Car():
     def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
     def Show(self):
      print("1st name is:",self.x,"2nd name is:",self.y,"3rd name is:",self.z)
mycar=Car("Toyota","Mehran","Civic")
mycar.Show()