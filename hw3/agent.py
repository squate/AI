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
#:::::Class Agent and related functions:::::
class Agent: #Initialize the Agent with Variables
    def __init__(self):
        self.name = "Bruce"
        self.locX = 0
        self.locY = 0
        self.stepCount = 0
        self.queue = []
        self.stack = []
        self.visited = []
        self.finalPath = []
        self.pathRecord = []
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
    def nodeToSquare(self,env,x,y):
        return x * env.getSideLength() + y
    def squareToNode(self,env,sqr):
        square = sqr
        l = env.getSideLength()
        x = int(square%l)
        y = int((square-x)/l)
        return env.nodes[x][y]
    def getFinalPath(self):
        return self.finalPath
#:::::movement up down left and right::::::
    def moveUp(self,env):
        log2("moving up from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY += 1
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveDown(self,env):
        log2("moving down from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locY -= 1
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
    def moveLeft(self,env):
        log2("moving left from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX -= 1
        self.stepCount += 1
        log("to "+ str(self.locX)+", "+str(self.locY)+")")
    def moveRight(self,env):
        log2("moving right from (" +str(self.locX)+", "+str(self.locY), " ")
        self.locX += 1
        self.stepCount += 1
        log("to "+str(self.locX)+", "+str(self.locY)+")")
#:::::Sensors::::::
    def expand(self,env,sqr):
        neighbors = []
        square = sqr
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                if self.squareToNode(env,i) != 1:
                    neighbors.append(i)
                #log(i)
        return neighbors
    #Find Heuristic Value of each square using Distance formula
    #this will probably be used for A*
    def findHyoo(self,env,x,y):
        goalx = env.getSideLength()-1
        goaly = env.getSideLength()-1
        #distance formula
        d = ((((goalx-x)**2) + ((goaly-y)**2))**(1/2.0))
        #print("distance from {0}{1} to goal is {2}".format(x,y,d))
        return d
    def squareToCoords(self, env, square):
        x = int(square%env.getSideLength())
        y = int((square - x)/env.getSideLength())
        return (x,y)
#:::::path-related functions:::::
    def trimPath(self,env):
        temp = []
        goal = self.pathRecord.pop()
        while goal[1]!=((env.getSideLength()**2)-1):
            goal = self.pathRecord.pop()
        log("Goal is {0}, and we got there from {1}".format(goal[1],goal[0]))
        temp.append(goal)
        while temp[0][0] != 0:
            for item in self.pathRecord:
                if item[1] == temp[0][0]:
                    temp.insert(0,item)
        log("this is the trimmed path{0}".format(temp))
        return temp
    def followPath(self,env):
        for i in range(len(self.finalPath)):
            xy0 = self.squareToCoords(env,self.finalPath[i][0])
            xy1 = self.squareToCoords(env,self.finalPath[i][1])
            x0, y0, x1, y1 = int(xy0[0]), int(xy0[1]), int(xy1[0]), int(xy1[1])
            log("(x0, y0): {0}".format(xy0))
            log("(x1, y1): {0}".format(xy1))
            if (x1 == x0):
                if (y1 > y0):
                    self.moveUp(env)
                else:
                    self.moveDown(env)
            else:
                if (x1 > x0):
                    self.moveRight(env)
                else:
                    self.moveLeft(env)

#:::::Search Algorithms:::::
    def DFS(self,env):
        #reset stack
        self.stack = [0]
        self.visited = []
        while (len(self.stack) > 0):
            parent = self.stack.pop();
            log("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                self.finalPath = self.trimPath(env)
                return True
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.stack:
                    self.stack.append(item)
                    self.pathRecord.append((parent,item))
                    log("added Square:{0}: to stack, stack is now {1}".format(item,self.stack))
            self.visited.append(parent)
    def BFS(self,env):
        #reset queue
        self.queue = [0]
        self.visited = []
        self.pathRecord = [(0,0)]
        while (len(self.queue) > 0):
            parent = self.queue.pop(0)
            print("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                log("Path record holds:{0}".format(self.pathRecord))
                self.finalPath = self.trimPath(env)
                return True
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.queue:
                    self.queue.append(item)
                    self.pathRecord.append((parent,item))
                    log("added Square:{0}: to Queue, Queue is now {1}".format(item,self.queue))
            self.visited.append(parent)
            start = parent
    def UCS(self,env):
        self.queue = [[0,[0,]]]
        self.visited =[]
        while (len(self.queue) > 0):
            log("current Queue {0}".format(self.queue))
            parent = self.queue.pop(0)
            log("parent is {0}".format(parent))
            log("parent[1] is {0}".format(parent[1]))
            if self.squareToNode(env,parent[1][len(parent[1])-1])==3:
                log("this is the path? {0}".format(parent[1]))
                self.finalPath = parent
                return parent
            for child in self.expand(env,parent[1][len(parent[1])-1]):
                if child in self.visited:
                    continue
                if child not in parent[1]:
                    log("adding Child:{0}: to parent".format(child))
                    temp = [parent[0]+1,(parent[1] + [child])]
                    log(" About to add temp = {0} to queue".format(temp))
                    self.queue.append(temp)
                    self.queue.sort()
                    log("element added is :{0}".format(temp))
            self.visited.append(parent)
        return
    def greed(self,env):
        return
    def aStar(self,env):
        return
