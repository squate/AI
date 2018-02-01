#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
from random import randint
from envi import *
DEBUG = False
#:::::logger:::::
def log(s):
    if DEBUG == True:
        print(s)
def log2(s,e):
    if DEBUG == True:

        print(s,end = e)

class Agent: #comment
#:::::Initialize the Agent with Variables:::::
    def __init__(self):
        self.name = "agent"
        self.age = 10
        self.locX = randint(0,9)
        self.locY = randint(0,9)
        self.speed = 1 #not yet susceptible to change by agent or environment
        self.succCount = 0
        self.stepCount = 0
#:::::Getters and Setters:::::
    def setName (self,name): #set method for name
        self.name = name
    def getName(self): #get method for name
        return self.name
    def getAge(self):
        return self.age
    def getlocX(self):
        return self.locX
    def getlocY(self):
        return self.locY
    def getspeed(self):
        return self.speed
    def getsuccCount(self):
        return self.succCount
    def getstepCount(self):
        return self.stepCount
#:::::movement up down left and right::::::
    def moveUp(self):
        log2("moving up from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY += self.speed
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveDown(self):
        log2("moving down from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY -= self.speed
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveLeft(self):
        log2("moving left from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX -= self.speed
        self.stepCount += 1
        log("to "+ str(self.locX)+", "+str(self.locY)+")")
    def moveRight(self):
        log2("moving right from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX += self.speed
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
#:::::succ necessity detection:::::
    def checkforSucc(self,envi): #determines whther or not to succ
        if envi.isdirty(self.locX, self.locY): #evaluate coord for need of succ()
            log2("Current square is dirty",", ")
            self.succ(envi)
            self.succCount += 1
#:::::clean current square:::::
    def succ(self, envi):
        log("imparting the succ to ("+ str(self.locX) + ", " + str(self.locY) + ") ")
        envi.succ(self.locX, self.locY)
#:::::reflex self-placement at the bneginning of a run.:::::
    def assumeThePosition(self, envi):
        while self.locX != 0: #while not touching the left wall
            self.checkforSucc(envi)
            self.moveLeft()
        while self.locY !=0: #while not touching the bottom wall
            self.checkforSucc(envi)
            self.moveDown()
#:::::determine action:::::
    def think(self, envi):
        x = self.getlocX()
        y = self.getlocY()
        s = envi.getSideLength()-1 #largest coordinate on either axis
        self.checkforSucc(envi)
        if y%2 == 0: #if the roomba is on an even column
            if x == (s): #if touching the right wall
                if y < (s): #if not already touching the top wall
                    self.moveUp()
            else:
                self.moveRight()
        else:
            if x == 0: #if touching the left wall
                if y < s: #if not already touching top wall
                    self.moveUp()
            else:
                self.moveLeft()
