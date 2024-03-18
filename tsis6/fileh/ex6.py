# for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     filename = x + ".txt"
#     file = open(filename, "w")  
#     file.write("This is file " + filename) 
#     file.close()

import string
import os
alphabet = string.ascii_uppercase
a = '/vs/PP2/A.txt'
os.remove(a)

for x in alphabet:
    filename = x + ".txt"
    file = open(filename, "w")
    file.write("This is file " + filename)