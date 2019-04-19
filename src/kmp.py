def KMPsearch(text, pat):
    txtLen = len(text)
    patLen = len(pat) #pat stands for pattern

    #preprocessing string 'pat'   
    longPS = [0]*patLen #array containing length of proper prefix and suffix
    i = 1
    lenSub = 0 #length of a substring that is both prefix and suffix

    while (i < patLen):
        if (pat[i] == pat[lenSub]):
            lenSub += 1
            longPS[i] = lenSub
            i += 1
        else:
            if (lenSub == 0):
                longPS[i] = 0
                i += 1
            else:
                lenSub = longPS[lenSub-1]

    i = 0
    j = 0 
    while (j < txtLen):
        if (text[i] == pat[j]):
            i += 1
            j += 1
        
        if (j == patLen):
            
