def myfunc(n):
    for i in range(len(n)-2):
        if n[i] == 0 and n[i+1] == 0 and n[i+2] == 7:
            return True
    return False

n = ([1,2,4,0,0,7,5]) 
# n = ([1,0,2,4,0,5,7])
# n = ([1,7,2,0,4,5,0]) 
print(myfunc(n))