# Please do your work for problem one in this file
#Matt Strayer
#Program that estimates the amount of ball filler needed for bowling balls

import math

def main():
    
    ballsManufactured = int(input("How many bowling balls will be manufactured?  "))
    diameterBall = float(input("What is the diameter of each ball in inches?  "))
    coreVolume =  int(input("What is the core volume in inches cubed?  "))

    ballVolume = 4/3 * math.pi * (diameterBall / 2)**3
    subtractCore = (ballVolume - coreVolume)
    amountFiller = (subtractCore * ballsManufactured)

    print("You will need", amountFiller," inches cubed of filler")
    
main()