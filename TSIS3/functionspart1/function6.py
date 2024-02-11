def reversing(string):
    words = []
    words = string.split()
    naoborot_words = reversed(words)  
    naoborot_sentence = ''.join(naoborot_words)  
    return naoborot_sentence


myinput = input("Vvedite sentense: ")
reversed_sentence = reversing(myinput)
print(reversed_sentence)

        