from random import randint
from sys import argv
import subprocess as sp 
sp.call('clear',shell=True) # clears the screen each time you need it

filename, storylength = argv

lowercase_vowels = [\
'a', \
'e', \
'i', \
'o', \
'a', \
'e', \
'e', \
'e', \
'e', \
'e', \
'i', \
'i', \
'o', \
'o', \
'u', \
'u', \
'y', \
'ee', \
'ei', \
'oa', \
'oo', \
'ea'] 

uppercase_vowels = [ \
'A', \
'A', \
'A', \
'E', \
'I', \
'I', \
'I', \
'I', \
'O', \
'U', \
'Y']

lowercase_consonants = [\
'b', \
'b', \
'b', \
'b', \
'c', \
'd', \
'd', \
'd', \
'd', \
'f', \
'g', \
'h', \
'j', \
'k', \
'l', \
'l', \
'l', \
'l', \
'l', \
'l', \
'l', \
'l', \
'm', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'n', \
'p', \
'que', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
'r', \
's', \
's', \
's', \
's', \
's', \
's', \
's', \
's', \
's', \
's', \
's', \
't', \
't', \
't', \
't', \
't', \
't', \
't', \
't', \
't', \
't', \
't', \
'v', \
'w', \
'x', \
'y', \
'z', \
'th', \
'ch', \
'st', \
'wr', \
'ph', \
'pr', \
'dr', \
'gh']

uppercase_consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Qu','R','S','T','V','W','X','Y','Z','Th','Ch','St','Wr','Ph','Pr','Dr']

lowercase_vowels_length = len(lowercase_vowels) - 1

punctuation = ['.', \
'.', \
'.', \
'.', \
'.', \
'.', \
'.', \
'.', \
'.', \
'!', \
'?']

occasional_nouns = [ \
'New York', \
'mouse', \
'dreaming' \
'random' \
'hello, world' \
]

sentenceLength = randint(1,20)

def randomVowel():
	return lowercase_vowels[randint(0,5)]
def letterGen(number):
	word = ""
	for i in range(0,number):
		word += randomVowel()
	return word

def midSentence(longest):
	sentenceWord = ""
	lowercase_consonant_length = len(lowercase_consonants) - 1
	wordMaxLength = randint(0,longest)
	if wordMaxLength < 2:
		return lowercase_vowels[randint(0,3)]
	else:
		for i in range(0,wordMaxLength):
			if i % 2 == 0:
				sentenceWord += lowercase_consonants[randint(0,lowercase_consonant_length)]
			else:
				sentenceWord += lowercase_vowels[randint(0,lowercase_vowels_length)]
		return sentenceWord

def startSentence(longest):
	sentenceWord = ""
	uppercase_consonant_length = len(uppercase_consonants) - 1
	lowercase_consonant_length = len(lowercase_consonants) - 1
	wordMaxLength = randint(0,longest)
	if wordMaxLength < 2:
		return uppercase_vowels[randint(0,5)]
	else:
		for i in range(0,wordMaxLength):
			if i == 0:
				sentenceWord += uppercase_consonants[randint(0,uppercase_consonant_length)]
			elif i % 2 == 0:
				sentenceWord += lowercase_consonants[randint(0,lowercase_consonant_length)]
			else:
				sentenceWord += lowercase_vowels[randint(0,5)]
		return sentenceWord

def sentence():
	internalSentence = []
	sLength = sentenceLength - 1
	internalSentence = startSentence(randint(1,10)),
	for i in range(1,sLength):
		internalSentence += midSentence(randint(1,10)),
	finalWord = midSentence(randint(1,10))
	return internalSentence

def paragraph(noOfSentences):
	finalPara = "\n\t"
	for i in range(1,noOfSentences):
		aSentence = sentence()
		finalPara += " ".join(aSentence) + ". "
	return finalPara

# print paragraph(5)
def story(noOfParagraphs):
	finalStory = ""
	for i in range(1,noOfParagraphs):
		finalStory += paragraph(randint(1,10))
	return finalStory		

def cutVowels():
	storyString = story(int(storylength))
	splitStoryString = storyString.split(' ')
	splitStoryStringLength = len(splitStoryString) - 1
	newStoryString = []
	if splitStoryString:
		for i in range(0,splitStoryStringLength):
			if len(splitStoryString[i]) != 1 and len(splitStoryString[i+1]) != 1 :
				newStoryString.append(splitStoryString[i])
			elif len(splitStoryString[i]) == 1 and splitStoryString[i] == "I" or splitStoryString[i] == "A":
				newStoryString.append(splitStoryString[i])
	nearlyFinalStory = " ".join(newStoryString)
	semifinalStoryList = nearlyFinalStory.split('.')
	finalStoryList = []
	for i in semifinalStoryList:
		randomPunct = punctuation[randint(0,len(punctuation)-1)]
		if len(i) > 2:
			if i[1].endswith(tuple(lowercase_consonants)) or i[1].endswith(tuple(lowercase_vowels)):
				finalStoryList.append(" " + uppercase_vowels[randint(0,len(uppercase_vowels)-1)] + i + randomPunct)  
			else:
				finalStoryList.append(i + randomPunct)
	finalStory = "".join(finalStoryList)
	print finalStory

cutVowels()


