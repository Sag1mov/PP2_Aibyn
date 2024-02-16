import math

def Squarepolyg(sn, len):
    S = (sn * len**2)/(4*math.tan(math.pi/sn))
    return S

sn = int(input())
len=  int(input())
Square = int(Squarepolyg(sn, len))
print(f"Square -> {Square}")