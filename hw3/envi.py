#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
# need to properly print grid, add roomba to display maybe
from random import randint
from array import array
from agent import *
import copy

#DEBUG = True

#def log(s):
#    if DEBUG == True:
#        print(s)

class envi:
    def __init__(self,n):
        self.sidelength = n
        self.nodes = [[0] * self.sidelength for i in range(self.sidelength)]
        self.nodes[self.sidelength-1][self.sidelength-1] = 3
        self.nodes[0][0] = 8
        self.walls = 7
        self.addWalls()
        self.edges = self.makeEdges(self.sidelength)

    def makeEdges(self,n): #needed for costs with the A* function
        w = n*n
        edgesGraph = [[0] * w for i in range(w)]
        #acct for adjancencies w/o walls
        for i in range(w):
            for j in range(w):
                if i%n == 0:
                    if (j == i+1 or j==i+n or j==i-n):
                        edgesGraph[i][j] = 1
                elif i%n == n-1:
                    if (j == i-1 or j==i+n or j==i-n):
                        edgesGraph[i][j] = 1
                else:
                    if (j == i-1 or j == i+1 or j == i+n or j == i-n):
                        edgesGraph[i][j] = 1
        #acct for walls
        for i in range(n):
            for j in range(n):
                if self.nodes[i][j]== 1:
                    index = int(n*j+i)
                    for e in range(w):
                        edgesGraph[index][e] = 0
                    for e in range(w):
                        edgesGraph[e][index] = 0
        return edgesGraph

    def isAdjacent(self, spot1, spot2):
        if self.edges[spot1][spot2] == 1:
            return True
        elif self.edges[spot1][spot2] == 0:
            return False

    def setSideLength(self,length):
        self.sidelength = length
    def getSideLength(self):
        return self.sidelength

    def visit(self,x,y):
        self.grid[x][y] = 2

    def squareNum(self,x,y):
        return grid[x][y]

    def addWalls(self):
        wallnum = 0
        while wallnum < self.walls:
            x = randint(0, self.sidelength-1)
            y = randint(0, self.sidelength-1)
            temp = self.nodes[x][y]
            if temp == 0:
                self.nodes[x][y] = 1
                wallnum += 1


    def showgrid(self, agent): #visual representation of the evironment. 1 represents a space that is dirty, 0 represents not so.
        grid2 = copy.deepcopy(self.nodes) #we looked this up because w/o, this messes up the counting due to how lists are
        grid2[agent.getlocX()][agent.getlocY()] = 2
        print("Showing Grid")
        for x in range(0,self.sidelength,1):
            gridline = ''.join(str(grid2[x]))
            print("x={0}:{1}".format(x,gridline))
    def showedges(self):
        print("Showing Edges")
        for x in range(0,(self.sidelength * self.sidelength),1):
            gridline = ''.join(str(self.edges[x]))
            print("Square{:2}:{:1}".format(x,gridline))
    def evaluate(self,agent):
        t = self.sidelength * self.sidelength
        s = agent.getstepCount()
        score = (s)/t
        print("score (less is better): " +str(score))
        return score
