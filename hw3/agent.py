#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
from random import randint
from envi import *
import math
import queue
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
        self.name = "Bruce"
        self.locX = 0
        self.locY = 0
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
#:::::algorithms:::::
def DFS(self,env):

class Node(self,env):
    def __init__(x,y,v):
        self.x = x
        self.y = y
        self.v = False
    def visit(self):
        self.v = True
#def aStar(self,env):
    #make tree starting from start

    #q = queue.PriorityQueue(0)
    #expand first in pq line
    #x = self.getlocX()
    #y = self.getlocY()
    #mtx = makeAdjMatrix(self,env)
    #cost = sqrt(pow((6-x),2)+(pow((6-y),2)))

    #while Node != g
        #if

def makeAdjList(self,env):
