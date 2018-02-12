#!/usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
from random import randint
from envi import *
import math


DEBUG = True
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
        self.name = "Bruce"
        self.locX = 2
        self.locY = 2
        self.stepCount = 0
        self.square = 14
        self.adj = []
        self.queue = []
        self.stack = []
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
    def getstepCount(self):
        return self.stepCount
    def setSquare(self,env):
        self.square = self.locX * env.getSideLength() + self.locY()
#:::::movement up down left and right::::::
    def findCoords(self, env,square):
        self.locX = square%env.getSideLength()
        self.locY = (square - self.locX)/env.getSideLength()
    def moveUp(self,env):
        log2("moving up from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY += self.speed
        self.stepCount += 1
        self.setSquare(env)
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveDown(self,env):
        log2("moving down from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY -= self.speed
        self.stepCount += 1
        self.setSquare(env)
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveLeft(self,env):
        log2("moving left from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX -= self.speed
        self.stepCount += 1
        self.setSquare(env)
        log("to "+ str(self.locX)+", "+str(self.locY)+")")
    def moveRight(self,env):
        log2("moving right from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX += self.speed
        self.stepCount += 1
        self.setSquare(env)
        log("to "+str(self.locX)+", "+str(self.locY)+")")
#:::::Sensors::::::
    def getAdjacencies(self,env):
        self.adj = []
        square = self.locX * env.getSideLength() + self.locY
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                self.adj.append(i)
                log(i)

#:::::algorithms:::::
