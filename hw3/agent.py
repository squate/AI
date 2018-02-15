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
        self.history = []
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
    def getHistory(self):
        return self.history
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
                if self.squareToNode(env,i) == 1:
                    print("this neighbor is a wall")
                #log(i)
        return self.adj
    def expand(self,env,sqr):
        neighbors = []
        square = sqr
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                if self.squareToNode(env,i) != 1:
                    neighbors.append(i)
                #log(i)
        return neighbors

    def makePath(self):
        path = []
        start = self.history[0]
        u = self.history.pop()
        path = []
        end = u[0]
        path.append(end)
        path.append(u[1])
        while end != start:
            for i in range(len(self.history)):
                if history[i][1] == end:
                    end = self.history[i][0]
                    path.insert(end,0)

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
        self.history = []
        self.queue = []
        self.visited = [0]
        self.queue += self.getAdjacencies(env)
        start = 0
        while len(self.queue) > 0:
            parent = self.queue.pop(0);
            end = parent
            self.history.append((start,end))
            print("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                return True
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.queue:
                    self.queue.append(item)
                    if self.squareToNode(env,parent) ==1:
                        print("about to add an item, taken from expand that is a wall")
                    print("added Square:{0}: to Queue, Queue is now {1}".format(item,self.queue))
            self.visited.append(parent)
            start = parent
            return self.makePath
