import os as os

def main():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(currentDir)
    os.chdir('..')

    #stopwordsList = open('data/stopwords.txt', 'r')
    stopwordsList = open('data\stopwords.txt', 'r')
    stopwordsList = stopwordsList.read().splitlines()

    userInput = input()
    userInput = userInput.split()

    resultString = ''

    for word in userInput:
        wordTemp = list(word)
        word = ''
        for char in wordTemp:
            if char is not '!' and char is not '?':
                word += char
        
        if word.lower() not in stopwordsList:
            resultString += word
            resultString += ' '
    
    resultTemp = list(resultString)
    resultTemp.pop()

    resultString = ''
    for char in resultTemp:
        resultString += char

    print(resultString)

main()