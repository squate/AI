#! /usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
# need to properly print grid, add roomba to display maybe
from random import randint
from array import array
from agent import *
import copy

def log(s):
    if DEBUG == True:
        print(s)

class envi:
    def __init__(self,n):
        self.sidelength = n
        self.grid = [[0] * self.sidelength for i in range(self.sidelength)]
        self.grid[self.sidelength-1][self.sidelength-1] = 3
        self.grid[0][0] = 8
        self.walls = 7
    def setSideLength(self,length):
        self.sidelength = length
    def getSideLength(self):
        return self.sidelength

    def visit(self,x,y):
        self.grid[x][y] = 2

    def addWalls(self):
        wallnum = 0
        while wallnum < self.walls:
            temp = self.grid[randint(0,self.sidelength)][randint(0,self.sidelength)]

            if temp == 0:
                temp = 1
                wallnum += 1


    def showgrid(self, agent): #visual representation of the evironment. 1 represents a space that is dirty, 0 represents not so.
        grid2 = copy.deepcopy(self.grid) #we looked this up because w/o, this messes up the counting due to how lists are
        grid2[agent.getlocX()][agent.getlocY()] = 2
        for x in range((self.sidelength-1),-1,-1):
            gridline = ''.join(str(grid2[x]))
            log(gridline)

    def evaluate(self,agent):
        t = self.sidelength * self.sidelength
        s = agent.getstepCount()
        score = (s)/t
        print("score (less is better): " +str(score))
        return score
