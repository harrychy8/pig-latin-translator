#-------------------------------------------------------------------------------
# Name:        coolest python assignment
# Purpose:      FOR FUN
#
# Author:      Harry 0802384
#
# Created:     20/11/2015
# Copyright:   (c) Harry Chen 0802384 2015
# Licence:     MIT
#
# As a WMCI Computer Science student, I state on my honour that I will:
# - cite any help that I have received (from other students, forums, etc.) on this assignment
# - not share actual program code with others. I realize that I am ENCOURAGED to discuss my approaches to solving problems, but that I should not share actual code.
#-------------------------------------------------------------------------------
import random
import re
finalscore = 0

def drawcards(cardid):

    top  =    " ____________ "
    side =    "|            |"
    #topnumber = "|  "+str([cardid[i]+1])+"       |"
    #botnumber = "|       "+str([cardid[i]]+1)+"   |"
    middle = ["|    ACE     |", #0 cardid
              "|    TWO     |", #1
              "|   THREE    |", #2
              "|    FOUR    |", #3
              "|    FIVE    |", #4
              "|    SIX     |", #5
              "|   SEVEN    |", #6
              "|   EIGHT    |", #7
              "|    NINE    |", #8
              "|    TEN     |", #9
              "|    JACK    |", #10
              "|   QUEEN    |", #11
              "|    KING    |"] #12

    bot =     "|____________|"


    newstr = ""
    #your problem is here.....
    for i in range(10):
        if i == 0: # if it's the top one
            for i in range(4):
                newstr += top + "         "
            newstr += "\n" #\n = newline char or [enter]
        elif i == 2: # if it's the topnumber
            for i in range(4):
                if cardid[i] < 9:
                    newstr += "|  "+str(cardid[i]+1)+ "         |" + "         "
                else:
                    newstr += "|  "+str(cardid[i]+1)+ "        |" + "         "
            newstr += "\n"
        elif i == 5: # if it's the middle one
            for i in range(4):
                 newstr += middle[cardid[i]] + "         "
            newstr += "\n"
        elif i == 8: #if it's the botnumber
            for i in range(4):
                if cardid[i] < 9:
                    newstr += "|         "+str(cardid[i]+1)+ "  |" + "         "
                else:
                    newstr += "|        "+str(cardid[i]+1)+ "  |" + "         "
            newstr += "\n"
        elif i == 9: # if it's the bottom one
            for i in range(4):
                newstr += bot + "         "
            newstr += "\n"
        else : # if it's everything else
            for i in range(4):
                newstr += side + "         "
            newstr += "\n"

    print(newstr) #print the card









def restartgame(finalscore):
    firstnumber = random.randint(1,12)
    secondnumber = random.randint(1,12)
    thirdnumber = random.randint(1,12)
    fourthnumber = random.randint(1,12)
    listofcards = [firstnumber,secondnumber,thirdnumber,fourthnumber]
    drawcards(listofcards)
    for i in range(4):
        listofcards[i]+=1
    passed = False
    while not passed:
        try:
            exp = input("please enter the expression using these 4 numbers to get to 24")
            answer = eval(exp)
            numbers = exp.replace("-","+").replace("*","+").replace("/","+").replace("(","+").replace(")","+").split("+")
            newnumbers = []
            for i in range(len(numbers)):
                if numbers[i] != '':
                    newnumbers.append(int(numbers[i]))
            print(newnumbers)
            print(listofcards)
            if len(newnumbers) == 4:
                for x in range(4):
                    if listofcards[x] != newnumbers[x]:
                        raise Exception("number not match!")
            else:
                raise Exception("number not match!")
            if answer != 24:
                raise Exception
            passed = True
        except Exception:
            print("Error")
    finalscore += 1
    print("YAY! You got it ! Would you like to try again?")


print("Welcome to 24 points game! Your goal is using the numbers on 4 cards to make an expression which can get 24! Remember, you cannot change the sequence of the 4 numbers. Click OK to continue!")

startinggame = False
while startinggame == False:
    try:
        play = input("Click OK to continue")
        if play =="":
            startinggame = True
    except Exception:
        pass

while startinggame == True:
    restartgame(finalscore)
    startinggame = False
    while startinggame == False:
        try:
            play = input("Click OK to try again")
            if play =="":
                startinggame = True
        except Exception:
            print("Thank You For Playing 24 Points!")
            print("Your Final Score is "+str(finalscore))
