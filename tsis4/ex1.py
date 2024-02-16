import math

def degtorad(degree):
    rad = degree * ((math.pi)/180)
    # rad = math.radians(degree)
    
    return rad

degree = float(input())
rad =degtorad(degree)
print(f"radian equal to -> {rad}") 
