import re

string1 = "This is a sample text with ab abob at the end."


proverka = r'(a+)(?:)b$'

x = re.findall(proverka, string1)

for i in x:
    print(i)



