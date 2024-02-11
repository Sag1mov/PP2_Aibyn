def pallindrom(string):
    if string ==  string[::-1]:
        return "It is pallindrom"
    else: 
        return "It is not"
    
    
string = input()
print(pallindrom(string))
    