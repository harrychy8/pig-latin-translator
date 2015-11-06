#-------------------------------------------------------------------------------
# Name:        translater
# Purpose:
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

def translate(word):
    vowels = ("aeiouyAEIOUY")
    translatedword = ""
    firstpart = ""
    secondpart = ""
    thirdpart = "ay"
    fourthpart = "yay"
    x = 0
    for character in word:
        if character not in vowels:
            secondpart += character
            x = x+1

        if character in vowels:
            if word[0] in vowels:
                firstpart += word[:len(word)]
                translatedword = firstpart + secondpart + fourthpart
            else:

                firstpart += word[x:len(word)]
                translatedword = firstpart + secondpart +thirdpart
    return translatedword


def flipWord(word):
    vowels = "aeiouy"
    word = word.lower()
    prefix = ""
    suffix = ""
    prefixDone = False
    for c in word:
        if not prefixDone and c in vowels:
            prefixDone = True
            suffix += c
        elif prefixDone:
            suffix += c
        else:
            prefix += c
    return suffix + prefix



print(flipWord("jack"))