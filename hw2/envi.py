#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
# need to properly print grid, add roomba to display maybe
from random import randint
from array import array
from agent import *
import copy
DEBUG = False
#:::::logger:::::
def log(s):
    if DEBUG == True:
        print(s)

class envi:
    def __init__(self):
        self.sidelength = 10
        self.grid = [[0] * self.sidelength for i in range(self.sidelength)]
        self.dirtynum = 0

    def setSideLength(self,length):
        self.sidelength = length
    def getSideLength(self):
        return self.sidelength
    def dirtleft(self):
        return self.dirtynum
    def isdirty(self, x, y):
        return self.grid[x][y]

    def superdirty(self): #IDK why i called it superdirty but it makes ~50% of the environment set to dirty.
        for x in range(0,self.sidelength):
            for y in range(0,self.sidelength):
                if randint(0,1)==1:
                    self.grid[x][y] = 1
                    self.dirtynum +=1

    def showgrid(self, agent): #visual representation of the evironment. 1 represents a space that is dirty, 0 represents not so.
        grid2 = copy.deepcopy(self.grid) #we looked this up because w/o, this messes up the counting due to how lists are
        grid2[agent.getlocX()][agent.getlocY()] = 2
        for x in range((self.sidelength-1),-1,-1):
            gridline = ''.join(str(grid2[x]))
            log(gridline)

    def evaluate(self,agent): #assign a score based on the roomba's reliability and efficiency
        d = self.dirtynum
        t = self.sidelength * self.sidelength
        s = agent.getstepCount()
        score = (s+d)/t
        log("score (less is better): " +str(score))
        return score

#:::::nate's attempts at adding shit:::::
    def succ(self,x,y): #the environment is affected by a roomba's succ
        #print("succ imparted at (" + str(x) + ", " +str(y) + ")")
        if self.isdirty(x,y) == 1:
            self.grid[x][y] = 0
            self.dirtynum -= 1
        else:
            self.grid[x][y] = 1
            self.dirtynum += 1
            log("no")
