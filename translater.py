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
    prefixDone = False
    for character in word:
        if not prefixDone and character in vowels:
            prefixDone = True
            suffix += character
        elif prefixDone:
            suffix += character
        else:
            prefix += character
    if word[0] in vowels:
        newword = suffix+prefix+"yay"
    else:
        newword = suffix+prefix+"ay"

    return newword

def fixword(word):
    capitalLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if word[0] in capitalLetter:
        newword = translateword(word)
        newword = newword.title()
        return newword
    else:
        newword = translateword(word)
        return newword


print(fixword("apple"))