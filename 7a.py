import math

class shape:
    def __init__(self):
        self.area=0
        self.name=""

    def showarea(self):
        print("the area of the",self.name,"is",self.area,"units")

class circle(shape):
    def __init__(self,radius):
        self.area=0
        self.name="circle"
        self.radius=radius

    def calcarea(self):
        self.area=math.pi*self.radius*self.radius

class rectangle(shape):
    def __init__(self,length,breadth):
        self.area=0
        self.name="rectangle"
        self.length=length
        self.breadth=breadth

    def calcarea(self):
        self.area=self.length*self.breadth

class triangle(shape):
    def __init__(self,base,height):
        self.area=0
        self.name="triangle"
        self.base=base
        self.height=height

    def calcarea(self):
        self.area=(self.base*self.height)/2

c1=circle(5)
c1.calcarea()
c1.showarea()
r1=rectangle(5,4)
r1.calcarea()
r1.showarea()
t1=triangle(3,4)
t1.calcarea()
t1.showarea()
    
        
    
