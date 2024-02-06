import math
class Point():
    def __init__(self, x, y, deltax, deltay):
        self.x = x
        self.y = y
        self.deltax = deltax
        self.deltay = deltay    
        
    def show(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")
    def move(self):
        print("(" + str(self.x+self.deltax) + "," + str(self.y+self.deltay) + ")")
    def dist(self):
        print(math.sqrt((self.x+self.deltax)**2+(self.y+self.deltay)**2))
        
x = int(input("x: "))
y = int(input("y: "))
deltax = int(input("deltax: "))
deltay = int(input("deltay: "))

output = Point(x,y, deltax, deltay)
output.show()
output.move()
output.dist()

    