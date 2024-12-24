def triple(word):
    new_word = ""
    for i in range (0,len(word)):
        new_word += word[i]*3
    print(new_word)




word = input("Enter a string: ")
triple(word)

#--------------------

def triple(word):
    new_word = []
    for i in range (0,len(word)):
        new_word += word[i]*3
        result = "".join(new_word) #The '' in front is the separator that you want to use between the elements when joining them.
    print(new_word)
    print(result)


word = input("Enter a string: ")
triple(word)

#-------------------------

def triple(word):
    new_word = []
    for i in range (0,len(word)):
        new_word.append( word[i]*3 )
        result = "".join(new_word) 
        result1 = "-".join(new_word) # The separator used here is "-" , so the elements will have "-" between them
    print(new_word)
    print(result)
    print(result1)

word = input("Enter a string: ")
triple(word)
