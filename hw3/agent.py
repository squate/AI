#!/usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
from random import randint
from envi import *
import math


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
        self.locX = 0
        self.locY = 0
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
    def canMove(self,env):
        self.adj=[]
        if self.y-1<env.sidelength:
            if env.grid[self.x][self.y-1]!=3:
                self.adj.append("D")
        if self.x+1<env.sidelength:
            if env.grid[self.x+1][self.y]!=3:
                self.adj.append("R")
        if self.x-1<env.sidelength:
            if env.grid[self.x-1][self.y]!=3:
                self.adj.append("L")
        if self.y+1<env.sidelength:
            if env.grid[self.x][self.y+1]!=3:
                self.adj.append("U")



#:::::algorithms:::::
#    def aStar(self,dungeon):
    def BFS(self, e):
        self.canMove(e)


class Square(object):
    def __init__(self,n,env,xCoord,yCoord):
        length = n
        x = xCoord
        y = yCoord
        name = str(x)+" "+str(y)
        r = Square(length, x+1, y) if ((x < (n-1))&&(env.squareNum(x+1,y)!=3)) else False
        u = Square(length, x, y+1) if ((y < (n-1))&&(env.squareNum(x,y+1)!=3)) else False
        l = Square(length, x-1, y) if ((x < 0)&&(env.squareNum(x-1,y)!=3)) else False
        u = Square(length, x, y+1) if ((y < 0)&&(env.squareNum(x,y-1)!=3)) else False
