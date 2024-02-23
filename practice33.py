class circle:
     def __init__(self):
        self.r=int(input("Enter the radius="))
     def get(self):
        self.a=2*3.141*self.r**2 
class cylinder(circle):
     def __init__(self):
        super().__init__()
        self.h=int(input("Enter the height"))
     def get(self): 
         self.b=2*3.141*self.r*self.h
     def cal(self):
         super().get()
         self.area=self.a+self.b
     def show(self):
        print("area of cylinder=",self.area)
a=cylinder()
a.get()
a.cal()
a.show()
