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
        self.locX = 0
        self.locY = 0
        self.stepCount = 0
        #self.square = 0
        self.adj = []
        self.queue = []
        self.stack = []
        self.visited = []
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
    def squareToNode(self,env,sqr):
        square = sqr
        l = env.getSideLength()
        x = int(square%l)
        y = int((square-x)/l)
        return env.nodes[x][y]
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
                #log(i)
        return self.adj
    def expand(self,env,sqr):
        neighbors = []
        square = sqr
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                neighbors.append(i)
                #log(i)
        return neighbors
#Find Heuristic Value of each square using Distance formula
    def findHyoo(self,env,x,y):
        goalx = env.getSideLength()-1
        goaly = env.getSideLength()-1
        #distance formula
        d = ((((goalx-x)**2) + ((goaly-y)**2))**(1/2.0))
        #print("distance from {0}{1} to goal is {2}".format(x,y,d))
        return d
#:::::algorithms:::::
    def DFS(self,env):
        #set visited to false for errything
        foundPath = False
        self.getAdjacencies(env)
        self.visited = []
        for i in range(0,len(self.adj)):
            self.stack.append(self.adj[i])
        while (len(self.stack) > 0) and foundPath == False:
            u = self.stack.pop();
            if self.squareToNode(env,u) == 3:
                print("found " + str(u))
                return u
            if u in self.visited:
                beenToU = True
            else:
                beenToU = False
            if beenToU == False:
                n = self.expand(env, u)
                self.visited.append(n)
                x = int(u%env.getSideLength())
                y = int((u-x)/env.getSideLength())
                env.visit(x,y)
                for i in range(0,len(n)):
                    if n[i] not in self.visited:
                        print("n{0} is {1}, which is not in list {2}".format(i,n[i],self.visited))
                        self.stack.append(n[i])
    def BFS(self,env):
        #reset flag and queue
        foundPath = False
        self.queue = []
        self.visited = [self.square]
        self.queue += self.getAdjacencies(env)
        while (len(self.queue) > 0) and foundPath == False:
            parent = self.queue.pop(0);
            print("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                return parent
            for item in self.queue:
                if item in self.visited:
                    continue
