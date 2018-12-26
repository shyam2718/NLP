import numpy 

f = open("Keywords.txt", "r")
    
for x in f:
    word = []
    for char in x:
        if char.isalpha() == True:
            word.append(char)

    word1 = (''.join(word)).lower()
    
    finale = "'" + word1 + "'" + ","   

    print(finale, end = "")
    

  
  