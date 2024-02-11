

# def permutations(string):
#     if len(string) == 1:
#         return [string]
    
#     permut = []
#     for i, char in enumerate(string):
#         substring = string[:i] + string[i+1:]
#         for p in permutations(substring):
#             permut.append(char + p)
    
#     for p in permut:
#         print(p)
            

def permutations(string):
    if len(string) == 1:
        return [string]
    
    permut = []
    for i, char in enumerate(string):
        substring = string[:i] + string[i+1:]
        for p in permutations(substring):
            permut.append(char + p)
    
    return permut


result = permutations(input())
for p in result:
    print(p)
