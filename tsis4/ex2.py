import math

def trapSquare(h, base1, base2):
    square = ((base1 + base2)/2) * h
    return square

h = float(input())
base1 = float(input())
base2 = float(input())

square = trapSquare(h, base1, base2)
print(f"Trapezoid square -> {square}")
