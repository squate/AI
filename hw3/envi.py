#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
# need to properly print grid, add roomba to display maybe
from random import randint
from array import array
from agent import *
import copy

DEBUG = False

def log(s):
    if DEBUG == True:
        print(s)
#:::::constructor:::::
class envi:
    def __init__(self, n, has_costs):
        self.sidelength = n
        self.nodes = [[0] * self.sidelength for i in range(self.sidelength)]
        self.nodes[self.sidelength-1][self.sidelength-1] = 3
        self.walls = 7
        self.addWalls()
        self.edges = self.makeEdges()
        if has_costs == True:
            self.costs = self.assignCosts()
#:::::setters and getters:::::
    def setSideLength(self,length):
        self.sidelength = length
    def getSideLength(self):
        return self.sidelength
    def makeEdges(self): #create adjacency matrix from nodes[][]
        n = self.sidelength
        w = n*n #amount of total squares
        edgesGraph = [[0] * w for i in range(w)]
        for i in range(w): #set all possible adjacencies to 1 in matrix
            for j in range(w):
                if i%n == 0:
                    if (j==i+1 or j==i+n or j==i-n):
                        edgesGraph[i][j] = 1
                elif i%n == n-1:
                    if (j==i-1 or j==i+n or j==i-n):
                        edgesGraph[i][j] = 1
                else:
                    if (j==i-1 or j==i+1 or j==i+n or j==i-n):
                        edgesGraph[i][j] = 1
        for i in range(n): #change connections involving walls to 0 in matrix
            for j in range(n):
                if self.nodes[i][j]==1:
                    index = int(n * j + i)
                    for e in range(w):
                        edgesGraph[index][e] = 0
                    for e in range(w):
                        edgesGraph[e][index] = 0
        return edgesGraph
    def assignCosts(self):
        costs = copy.deepcopy(self.edges)
        for i in range(self.sidelength*self.sidelength):
            for j in range(self.sidelength*self.sidelength):
                costs[i][j] = random.randint(1, 20)
        return costs
    def getCost(self,origin,destination):
        return int(self.costs[origin][destination])
    def resetEverythingButCosts(self):
        for i in range(self.sidelength):
            for j in range(self.sidelength):
                self.nodes[i][j] = 0
        self.nodes[self.sidelength-1][self.sidelength-1] = 3
        self.addWalls()
        self.edges = self.makeEdges()
    def visit(self,x,y):
        log("visiting{0},{1}".format(x,y))
        self.nodes[x][y] = 2
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
        grid2[agent.getlocX()][agent.getlocY()] = 8
        print("Showing Grid")
        for x in range(0,self.sidelength,1):
            gridline = ''.join(str(grid2[x]))
            print("x={0}:{1}".format(x,gridline))
    def showedges(self):
        print("Showing Edges")
        for x in range(0,(self.sidelength * self.sidelength),1):
            gridline = ''.join(str(self.edges[x]))
            print("Square{:2}:{:1}".format(x,gridline))
