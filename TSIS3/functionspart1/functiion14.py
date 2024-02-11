import random
from function6 import reversed_sentence
from function10 import function

def main():
    s = input()
    reversing = reversed_sentence(s)
    print("result",  reversing)
    
    list1 = [1, 2, 2, 3, 4, 4, 5, 7] 
    list2 =  function(list1)
    print("first list was", list1, "unique list", list2)
    

if __name__ == "__main__":
    main()
    