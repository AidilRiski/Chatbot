import re as regex;

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
#Output: Kumpulan string pada _stringToCheck yang memenuhi regular expression pada _pattern.
#Memakai Regular Expression
def stringMatchRegex(_pattern, _stringToCheck):
    _temp = _pattern.split()
    _pattern = ''

    count = 0
    for _elmt in _temp:
        _pattern += _elmt
        if (count < len(_temp) - 1):
            _pattern += ' '
            _pattern += '[\w\s]{0,20}?'
        count += 1
    
    print(_pattern)
    print(_stringToCheck)
    return regex.findall(_pattern, _stringToCheck)

def main():
    userInput = input()
    userInput2 = input()
    print(stringMatchRegex(userInput, userInput2))

main()