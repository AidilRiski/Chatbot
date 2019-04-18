import enum as enum
import re as regex
import csv as csv
import os as os

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
    realPattern = _pattern

    temp = _pattern.split()
    _pattern = ''

    count = 0
    for elmt in temp:
        _pattern += elmt
        if (count < len(temp) - 1):
            _pattern += ' '
            _pattern += '[\w\s]{0,20}?'
        count += 1
    
    matchRegex = regex.match(_pattern, _stringToCheck)
    if matchRegex is None:
        return 0
    
    sameChars = 0
    for character in realPattern:
        if character in _stringToCheck:
            sameChars += 1
    
    return sameChars / len(_stringToCheck)

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

def main():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(currentDir)
    os.chdir('..')
    faqIndonesia = []
    with open('data/faqIndonesia.txt', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            faqIndonesia.append(row)
    os.chdir('src/')

    userInput = input()
    results = findSuitable(userInput, faqIndonesia, SolveMethod.Regex)

    if (len(results) == 1):
        print(results[0][1])
    elif (len(results) > 1):
        print('Ditemukan beberapa pertanyaan yang sesuai: ')
        count = 1
        for result in results:
            print('[' + count + '] ' + result[0][0])

        print('Pilih pertanyaan yang sesuai!')
        userInput = input()

        print(result[int(userInput) - 1][1])
    return

main()