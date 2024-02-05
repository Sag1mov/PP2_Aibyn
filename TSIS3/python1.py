class foractionString():
    def __init__(self, getString):
        x = getString.upper()
        self.getString = x
        
    
    def printString(self):
        print(self.getString)
        
getString = input()
answer = foractionString(getString)
answer.printString()