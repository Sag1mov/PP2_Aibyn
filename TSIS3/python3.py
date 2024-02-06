
class Shape():
    def __init__(self, width, length):
        self.width =  width
        self.length = length
        
    def Area(self):
        self.area = self.width * self.length
        return f"Area is: {self.area}"
        
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__(width, length)
    
    
inpwidth = int(input("width:"))
inplenth = int(input("length:"))
area =  Rectangle(inpwidth, inplenth)
print(area.Area())