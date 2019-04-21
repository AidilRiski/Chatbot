import enum as enum
import re as regex
import csv as csv
import os as os
import sys as sys
import itertools as itool

currentDir = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)
os.chdir('..')

sys.path.append('src/tesaurus-master')

import tesaurus as tes

class SolveMethod(enum.Enum):
    KMP = 0
    BoyerMoore = 1
    Regex = 2

#Input: Sebuah string _pattern yang akan dicari pada sebuah string _stringToCheck.
#Output: Persentasi kemiripan maksimal. (Jumlah karakter yang sama berurutan dibagi panjang _stringToCheck).
#Memakai metode KMP
def stringMatchKMP(_pattern, _stringToCheck):
    print('checking ' + _pattern + ' toward ' + _stringToCheck)
    realPattern = _pattern.lower()
    stringToCheckClean = _stringToCheck.lower()

    txtLen = len(stringToCheckClean)
    patLen = len(realPattern) #pat stands for pattern
    
    #preprocessing string 'realPattern'   
    longPS = [0]*patLen #array containing length of proper prefix and suffix
    i = 1
    lenSub = 0 #length of a substring that is both prefix and suffix
    found = False

    while (i < patLen):
        if (realPattern[i] == realPattern[lenSub]):
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
        print('checking ' + _pattern + ' toward ' + _stringToCheck)
        print('i ' + str(i))
        print('j ' + str(j))
        if (stringToCheckClean[j] == realPattern[i]):
            i += 1
            j += 1
        
        if (i == patLen):
            found = True
            i = longPS[i-1]
        elif j < txtLen and realPattern[i] != stringToCheckClean[j]:
            if i != 0:
                i = longPS[i-1]
            else:
                i += 1

    similarityPercentage = 0
    if (found):
        similarityPercentage = patLen / txtLen
        
    return similarityPercentage

#Input: Sebuah string _pattern yang akan dicari pada sebuah string _stringToCheck.
#Output: Persentasi kemiripan maksimal. (Jumlah karakter yang sama berurutan dibagi panjang _stringToCheck).
#Memakai metode Boyer-Moore
def stringMatchBoyerMoore(_pattern, _stringToCheck):
    realPattern = _pattern.lower()
    stringToCheckClean = _stringToCheck.lower()
    last= buildLast(stringToCheckClean)
    n = len(realPattern)
    m = len(stringToCheckClean)
    count=0
    max=0
    i = m-1
    #print('Checking ' + _pattern + ' toward ' + _stringToCheck)
    if(i > n-1): #Pattern lebih panjang daripada text
        temp=stringMatchBoyerMoore(stringToCheckClean,realPattern)
        if(temp>0.9):
            #print('C ' + str(1))
            return 1
        else:
            #print('D ' + str(0))
            return 0
    else:
        j = m-1
        while True:
            if (stringToCheckClean[j] == realPattern[i]):
                count+=1
                if (j == 0):
                    #print('A ' + str((count+1)/n))
                    return (count+1)/n; # match
                else: # looking-glass technique
                    i-=1
                    j-=1
            else : # character jump technique
                lo = last[ord(realPattern[i])]
                i = i + m - min(j, 1+lo)
                j = m-1  
                if(count>max):
                    max=count
                count=0
            if (i > n-1) :
                break
                # no match
    similarityPercentage = max/n
    #print('B ' + str(similarityPercentage))
    return similarityPercentage

def buildLast(pattern):
    #Return array storing index of last
    #occurrence of each ASCII char in pattern.
    last = [-1]*128
    for i in range(0,len(pattern)):
        last[ord(pattern[i])]=i
    return last

#Input: Sebuah string _pattern yang akan dicari pada sebuah string _stringToCheck.
#Output: Persentasi kemiripan maksimal. (Jumlah karakter yang sama berurutan dibagi panjang _stringToCheck).
#Memakai Regular Expression
def stringMatchRegex(_pattern, _stringToCheck):
    realPattern = _pattern.lower()
    stringToCheckClean = _stringToCheck.lower()

    temp = _pattern.split()
    _pattern = ''

    count = 0
    for elmt in temp:
        _pattern += elmt.lower()
        if (count < len(temp) - 1):
            _pattern += ' '
            _pattern += '[\w\s]{0,20}?'
        count += 1
    
    matchRegex = regex.match(_pattern, stringToCheckClean)
    if matchRegex is None:
        return 0
    
    sameChars = 0
    for character in realPattern:
        if character in stringToCheckClean:
            sameChars += 1
    
    return sameChars / len(stringToCheckClean)

def joinStringCSV(csvReader):
    returnValue = ''
    count = 0
    for string in csvReader:
        returnValue += string[0]
        if (count < len(csvReader) - 1):
            returnValue += ' '
        count += 1
    return returnValue

def normalizeTuple(_tuple):
    returnValue = ''
    for elmt in _tuple:
        if type(elmt) == tuple:
            returnValue += normalizeTuple(elmt)
        else:
            returnValue += ' ' + elmt

    return returnValue

def cleanString(_string):
    tempList = []
    tempList = _string.split()

    count = 0
    returnValue = ''
    for elmt in tempList:
        returnValue += elmt
        if count < len(tempList) - 1:
            returnValue += ' '
        count += 1

    return returnValue

def findSuitable(_pattern, _csvData, _solveMethod):
    returnValue = []
    patternSynonyms = []
    patternExplode = _pattern.split()
    for word in patternExplode:
        sinonimList = tes.getSinonim(word)
        sinonimList.append(word)
        patternSynonyms.append(sinonimList)
    
    patternStringList = ['']
    for listElmt in patternSynonyms:
        patternStringList = itool.product(patternStringList, listElmt)

    patternStringSynonims = []
    for tupleElmt in patternStringList:
        patternStringSynonims.append(cleanString(normalizeTuple(tupleElmt)))
    
    print(patternStringSynonims)

    if (_solveMethod == SolveMethod.Regex):
        for data in _csvData:
            for querySynonym in patternStringSynonims:
                similarityVal = stringMatchRegex(querySynonym, data[0])
                #print('Sim ' + str(similarityVal))
                if (similarityVal >= 0.9):
                    print('Found ' + querySynonym + ' ' + data[0])
                    returnValue.append(data)
    elif (_solveMethod == SolveMethod.KMP):
        for data in _csvData:
            for querySynonym in patternStringSynonims:
                similarityVal = stringMatchKMP(querySynonym, data[0])
                print('Sim ' + str(similarityVal))
                if (similarityVal >= 0.9):
                    print('Found ' + querySynonym + ' ' + data[0])
                    returnValue.append(data)
    elif (_solveMethod == SolveMethod.BoyerMoore):
        for data in _csvData:
            for querySynonym in patternStringSynonims:
                similarityVal = stringMatchBoyerMoore(querySynonym, data[0])
                #print('Sim ' + str(similarityVal))
                if (similarityVal >= 0.9):
                    print('Found ' + querySynonym + ' ' + data[0])
                    returnValue.append(data)
    
    realReturnValue = []
    for sentence in returnValue:
        if sentence not in realReturnValue:
            realReturnValue.append(sentence)
    
    return realReturnValue

def sanitizeStopWords(_string, _stopwordsList):
    _string = _string.split()
    returnValue = ''

    for word in _string:
        wordTemp = list(word)

        word = ''
        for char in wordTemp:
            if char is not '!' and char is not '?':
                word += char

        if word.lower() not in _stopwordsList:
            returnValue += word
            returnValue += ' '
    
    returnValueTemp = list(returnValue)
    returnValueTemp.pop()
    
    returnValue = ''
    for char in returnValueTemp:
        returnValue += char

    '''
    _string = _string.split()
    _tempString = []

    for word in _string:
        _tempString.append(word)

    for word in _tempString:
        if word.lower() in _stopwordsList:
            _string.remove(word)

    returnValue = ''
    count = 0
    for word in _string:
        returnValue += word
        if count < len(_string) - 1:
            returnValue += ' '
        count += 1
    '''

    return returnValue

def main():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(currentDir)
    os.chdir('..')

    faqIndonesia = []
    csvFile =  open('data/faqIndonesia.txt', 'r')
    reader = csv.reader(csvFile)
    for row in reader:
        faqIndonesia.append(row)

    txtFile = open('data/stopwords.txt', 'r')
    txtFile = txtFile.read().splitlines()

    argCount = 0
    argVector = []
    userInput = ''
    solveMethodStr = ''
    for arg in sys.argv:
        if argCount == 1:
            solveMethodStr = arg
        if argCount > 1:
            argVector.append(arg)
        argCount += 1

    solveMethod = None
    if solveMethodStr == 'kmp':
        solveMethod = SolveMethod.KMP
    elif solveMethodStr == 'boy':
        solveMethod = SolveMethod.BoyerMoore
    elif solveMethodStr == 'reg':
        solveMethod = SolveMethod.Regex

    for elmt in argVector:
        argCount -= 1
        userInput += elmt
        if argCount > 1:
            userInput += ' '
    
    userInput = sanitizeStopWords(userInput, txtFile)
    results = findSuitable(userInput, faqIndonesia, solveMethod)

    fileWriter = open('data/result.txt', 'w+')

    for result in results:
        fileWriter.write(result[0] + ',' + result[1] + '\n')

    if (len(results) == 1):
        print(results[0][1])
    elif (len(results) > 1):
        print('Ditemukan beberapa pertanyaan yang sesuai: ')
        count = 1
        for result in results:
            print('[' + str(count) + '] ' + result[0])
            count += 1

        print('Pilih pertanyaan yang sesuai!')
        userInput = input()

        print(results[int(userInput) - 1][1])

    os.chdir('src/')
    return

main()