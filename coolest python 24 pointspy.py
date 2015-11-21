#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      0802384
#
# Created:     20/11/2015
# Copyright:   (c) 0802384 2015
# Licence:     <your licence>
#
# As a WMCI Computer Science student, I state on my honour that I will:
# - cite any help that I have received (from other students, forums, etc.) on this assignment
# - not share actual program code with others. I realize that I am ENCOURAGED to discuss my approaches to solving problems, but that I should not share actual code.
#-------------------------------------------------------------------------------
import random

def drawcards(cardid):

    top  =    " ____________ "
    side =    "|            |"

    middle = ["|    ACE     |", #0 cardid
              "|    TWO     |", #1
              "|   THREE    |", #2
              "|    FOUR    |", #3
              "|    FIVE    |", #4
              "|    SIX     |", #5
              "|   SEVEN    |", #6
              "|    EIGHT   |", #7
              "|    NINE    |", #8
              "|     TEN    |", #9
              "|    JACK    |", #10
              "|   QUEEN    |", #11
              "|    KING    |"] #12

    bot =     "|____________|"


    str = ""
    #your problem is here.....
    for i in range(10): #loop 10 times
        if i == 0: # if it's the top one
            for i in range(4):
                str += top + " "
            str += "\n" #\n = newline char or [enter]
        if i == 4: # if it's the middle one
            for i in range(4):
                str += middle[cardid[i]] + " "
            str += "\n"
        if i == 9: # if it's the bottom one
            for i in range(4):
                str += bot + " "
            str += "\n"
        else : # if it's everything else
            for i in range(4):
                str += side + " "
            str += "\n"

    print(str) #print the card



def drawgroupofcards(firstnumber,secondnumber,thirdnumber,fourthnumber):
    newstring ="" #what is this???

    drawcards([firstnumber,secondnumber,thirdnumber,fourthnumber]) #we put id into an array, it's easier to loop through




def restartgame():
    firstnumber = random.randint(1,12)
    secondnumber = random.randint(1,12)
    thirdnumber = random.randint(1,12)
    fourthnumber = random.randint(1,12)
    drawgroupofcards(firstnumber,secondnumber,thirdnumber,fourthnumber)

restartgame()