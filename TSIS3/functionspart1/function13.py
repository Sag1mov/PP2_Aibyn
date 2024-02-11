import random

def guessing():
    n = random.randint(1, 20)
    popytka = 0
    
    print("Please try to guess number in range from 1 to 20")
    i =1 
    while i == 1:
        tryf = int(input("Enter number->"))
        popytka += 1
        
        if n == tryf:
            print("ВЫ УГАДАЛИ")
            break
        elif n > tryf:
            print("загаданное число больше, еще попытка") 
        elif n < tryf:
            print("загаданное число меньше, еще попытка")
            
            
guessing()