def myfunc(n):
    for i in range(len(n)-1):
        if n[i] == 3 and n[i+1] == 3:
            return True
    return False

n = ([1, 3, 3]) 
# n = ([1, 3, 1, 3]) 
# n = ([3, 1, 3]) 
print(myfunc(n))