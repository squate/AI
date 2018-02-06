#!~/usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
from random import randint
from envi import *
#DEBUG = False
#:::::logger:::::
#def log(s):
#    if DEBUG == True:
#        print(s)
#def log2(s,e):
#    if DEBUG == True:
#        print(s,end = e)

class Agent: #comment
#:::::Initialize the Agent with Variables:::::
    def __init__(self):
        self.name = "Bruce"
        self.locX = randint(0,9)
        self.locY = randint(0,9)
        self.stepCount = 0
        self.adj=[]
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
#:::::Sensors::::::
    def isWall(self,env,x,y):
        if env.grid[x][y]==3 :
            return True
        else:
            return False
#    def canMove(self,env):
        
#:::::algorithms:::::
#    def aStar(self,dungeon): 
