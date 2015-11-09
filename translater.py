#-------------------------------------------------------------------------------
# Name:        translator
# Purpose:      comp sci 20 assiment
#
# Author:      0802384 Harry
#
# Created:     05/11/2015
# Copyright:   (c) Harry 2015
# Licence:     <your licence>
#
# As a WMCI Computer Science student, I state on my honour that I will:
# - cite any help that I have received (from other students, forums, etc.) on this assignment
# - not share actual program code with others. I realize that I am ENCOURAGED to discuss my approaches to solving problems, but that I should not share actual code.
#-------------------------------------------------------------------------------

# translator first step --- translate the word
def translateword(word):
    vowels = "aeiouyAEIOUY"
    word = word.lower()
    prefix = ""
    suffix = ""
    newword = ""

    #check the puctuation (only include . , ! ? here)
    punctuation = ",.!?"
    newpunctuation = ""
    if word[len(word)-1] in punctuation:
        newpunctuation = word[len(word)-1]
        word = word[0:len(word)-1]
    else:
        pass

    prefixDone = False

    #check and translate the word
    for character in word:
        if not prefixDone and character in vowels:
            prefixDone = True
            suffix += character
        elif prefixDone:            suffix += character
        else:
            prefix += character

    # check first letter
    if word[0] in vowels:
        newword = suffix+prefix+"yay"+newpunctuation
    else:
        newword = suffix+prefix+"ay"+newpunctuation

    return newword


# fix those upper cased letter
def fixword(word):
    capitalLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if word[0] in capitalLetter:
        newword = translateword(word)
        newword = newword.title()
    else:
        newword = translateword(word)

    return newword

print(fixword("happy!"))

#get all the words in one sentence
def split_sentence(sentence):
    words = sentence.split() #split by space
    alphabet = "abcdefghijklmnopqrstuvwxyz,.!?"
    alphabet += alphabet.upper() #now alphabet is "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #get rid off all non-alphabet characters in words
    newWords = []
    for word in words:
        newWord = ""
        for c in word:
            if c in alphabet:
                newWord += c
        newWords.append(newWord)
    print(newWords)
    return newWords


wordList = split_sentence("this Is an example seNtenCe, wEll I mEAn. Hahahh!")
sentence = ""
for word in wordList:
    sentence += fixword(word) + " "

print(sentence)