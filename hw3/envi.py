#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
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
        self.nodes = [[0] * self.sidelength for i in range(self.sidelength)]
        self.nodes[self.sidelength-1][self.sidelength-1] = 3
        self.nodes[0][0] = 8
        self.walls = 7
        self.addWalls()
        self.edges = self.makeEdges(self.sidelength)

    def makeEdges(self,n):
        w = n*n
        edges = [[0] * w for i in range(w)]
        #acct for adjancencies w/o walls
        for i in range(w):
            for j in range(w):
                if i%n == 0:
                    if (j == i+1||j==i+n||j==i-n):
                        edges[i][j] = 1
                elif i%n == n-1:
                    if (j == i-1||j==i+n||j==i-n):
                        edges[i][j] = 1
                else:
                    if (j == i-1||j == i+1||j == i+n||j == i-n):
                        edges[i][j] = 1
        #acct for walls
        for i in range(n):
            for j in range(n):
                if nodes[i][j]== 3:
                    oof = n*nodes[i]+nodes[j]
                    for e in range(w):
                        edges[oof][e] == 0
                    for e in range(w):
                        edges[e][oof] == 0

    def isAdjacent(self, spot1, spot2):
        if edges[spot1][spot2] == 1:
            return True
        elif edges[spot1][spot2] == 0:
            return False

    def setSideLength(self,length):
        self.sidelength = length
    def getSideLength(self):
        return self.sidelength

    def visit(self,x,y):
        self.grid[x][y] = 2

    def addWalls(self):
        wallnum = 0
        while wallnum < self.walls:
            temp = self.nodes[randint(0,self.sidelength)][randint(0,self.sidelength)]

            if temp == 0:
                temp = 1
                wallnum += 1


    def showgrid(self, agent): #visual representation of the evironment. 1 represents a space that is dirty, 0 represents not so.
        grid2 = copy.deepcopy(self.nodes) #we looked this up because w/o, this messes up the counting due to how lists are
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
=======
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
