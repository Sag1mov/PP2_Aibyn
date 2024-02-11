def function(n1):
    n2 = []
    for a in n1:
        if a not in n2:
            n2.append(a)
    return n2
  
  
n1 = [1, 2, 3, 3, 4, 4, 5]          
result = function(n1)
print(result)
                
