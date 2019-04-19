import enum as enum
import re as regex
import csv as csv
import os as os
import sys as sys

class SolveMethod(enum.Enum):
    KMP = 0
    BoyerMoore = 1
    Regex = 2

#Input: Sebuah string _pattern yang akan dicari pada sebuah string _stringToCheck.
#Output: Persentasi kemiripan maksimal. (Jumlah karakter yang sama berurutan dibagi panjang _stringToCheck).
#Memakai metode KMP
def stringMatchKMP(_pattern, _stringToCheck):
    similarityPercentage = 0
    return similarityPercentage

#Input: Sebuah string _pattern yang akan dicari pada sebuah string _stringToCheck.
#Output: Persentasi kemiripan maksimal. (Jumlah karakter yang sama berurutan dibagi panjang _stringToCheck).
#Memakai metode Boyer-Moore
def stringMatchBoyerMoore(_pattern, _stringToCheck):
    similarityPercentage = 0
    return similarityPercentage

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

def findSuitable(_pattern, _csvData, _solveMethod):
    returnValue = []
    if (_solveMethod == SolveMethod.Regex):
        for data in _csvData:
            similarityVal = stringMatchRegex(_pattern, data[0])
            if (similarityVal >= 0.9):
                returnValue.append(data)
        
    return returnValue

def sanitizeStopWords(_string, _stopwordsList):
    _string = _string.split()
    returnValue = ''

    for word in _string:
        wordTemp = list(word)

        word = ''
        for char in wordTemp:
            if char is not '!' and char is not '?':
                word += char

        if word not in _stopwordsList:
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
    for arg in sys.argv:
        if argCount > 0:
            argVector.append(arg)
        argCount += 1

    for elmt in argVector:
        argCount -= 1
        userInput += elmt
        if argCount > 0:
            userInput += ' '
    
    userInput = sanitizeStopWords(userInput, txtFile)
    print(userInput)
    results = findSuitable(userInput, faqIndonesia, SolveMethod.Regex)

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