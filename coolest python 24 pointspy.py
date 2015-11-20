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
# - be ready to explain any parts of the code I submit. I know that if I donâ€™t understand what something does, it doesnâ€™t belong in my assignment.
#-------------------------------------------------------------------------------
import random

def drawcards(cardnumber):

    top = " ____________"
    side = "|            |"
    if cardnumber >=10:
        numbers = "|     "+str(cardnumber)+  "     |"
    else:
        numbers = "|     "+str(cardnumber)+  "      |"
    middle = ["|    ACE     |","|    TWO     |","|   THREE    |","|    FOUR    |","|    FIVE    |","|    SIX     |","|   SEVEN    |","|    EIGHT   |","|    NINE    |","|     TEN    |","|    JACK    |","|   QUEEN    |","|    KING    |"]
    bot = "|____________|"

    print(top)
    print(side)
    print(side)
    print(numbers)
    print(side)
    print(middle[cardnumber-1])
    print(side)
    print(numbers)
    print(side)
    print(side)
    print(bot)


def drawgroupofcards(firstnumber,secondnumber,thirdnumber,fourthnumber):
    newstring =""

    newstring += str(drawcards(firstnumber))+"                "+str(drawcards(secondnumber))+"                 "+str(drawcards(thirdnumber))+"                  "+str(drawcards(fourthnumber))





def restartgame():
    firstnumber = random.randint(1,13)
    secondnumber = random.randint(1,13)
    thirdnumber = random.randint(1,13)
    fourthnumber = random.randint(1,13)
    drawgroupofcards(firstnumber,secondnumber,thirdnumber,fourthnumber)

restartgame()