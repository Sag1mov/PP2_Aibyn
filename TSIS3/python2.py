class Shape:
    def Area():
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def Area(self):
        print(self.length**2)
    
s1 = Square(5)
s1.Area()