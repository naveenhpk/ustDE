'''write  a Python class named Rectangle constructed by a length and width and
 a method which will  compute the area and perimeter of a rectangle'''

class Rectangle:
    def __init__(self,l,b):
        self._length=l
        self._breadth=b
    def area(self):
        print("Area",self._length*self._breadth)
    def perimeter(self):
        print("Perimeter",2*(self._breadth+self._length))

r=Rectangle(20,30)
r.area()
r.perimeter()