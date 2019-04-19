# ==================================================
# Written in March 2016 by Victoria Anugrah Lestari
# ==================================================
import json
import os
import sys

# ==================================================
# Membaca dictionary dari json
# ==================================================
def load(filename):	
	with open(filename) as data_file:
		data = json.load(data_file)	

	return data

# load dictionary
currentDir = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentDir)
mydict = load('dict.json')
os.chdir('../..')

# ==================================================
# Mencari sinonim suatu kata
# ==================================================
def getSinonim(word):
	if word in mydict.keys():
		return mydict[word]['sinonim']
	else:
		return []

# ==================================================
# Mencari antonim suatu kata
# ==================================================
def getAntonim(word):
	if word in mydict.keys():
		if 'antonim' in mydict[word].keys():
			return mydict[word]['antonim']

	return []
