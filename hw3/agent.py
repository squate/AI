#!/usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
from random import randint
from envi import *
import math
import queue
import random
import operator

DEBUG = False
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
        self.list = []
        self.visited = []
        self.pathRecord = []
        self.finalPath = []
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
    def getFinalPath(self):
        return self.finalPath
#:::::converting between squares and nodes:::::
    def nodeToSquare(self,env,x,y):
        return x * env.getSideLength() + y
    def squareToCoords(self, env, square):
        x = int(square%env.getSideLength())
        y = int((square - x)/env.getSideLength())
        return (x,y)
    def squareToNode(self,env,square):
        l = env.getSideLength()
        x = int(square%l)
        y = int((square-x)/l)
        return env.nodes[x][y]
#:::::movement (up, down, left and right):::::
    def moveUp(self,env):
        self.visit(env)
        log2("Moving UP        (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locY += 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def moveDown(self,env):
        self.visit(env)
        log2("Moving DOWN      (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locY -= 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def moveLeft(self,env):
        self.visit(env)
        log2("Moving LEFT      (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locX -= 1
        log("--> ("+ str(self.locX)+", "+str(self.locY)+")")
    def moveRight(self,env):
        self.visit(env)
        log2("Moving RIGHT     (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locX += 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def visit(self,env):
        log("visiting ({0}, {1})".format(self.locX,self.locY))
        env.visit(self.locX,self.locY)
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
    def findHyoo(self,env,square):
        x = int(square%env.sidelength)
        y = int((square-x)/env.sidelength)
        goalx = env.getSideLength()-1
        goaly = env.getSideLength()-1
        #distance formula
        d = ((((goalx-x)**2) + ((goaly-y)**2))**(1/2.0))
        log("distance from {0} to goal is {1}".format(square,d))
        return d
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
        self.locX = 0
        self.locY = 0
        log("following path:\n{0}".format(self.finalPath))
        for i in range(len(self.finalPath)):
            xy0 = self.squareToCoords(env,self.finalPath[i][0])
            xy1 = self.squareToCoords(env,self.finalPath[i][1])
            x0, y0, x1, y1 = int(xy0[0]), int(xy0[1]), int(xy1[0]), int(xy1[1])
            if (x1 == x0):
                if (y1 > y0):
                    self.moveUp(env)
                else:
                    self.moveDown(env)
            else:
                if (x1 > x0):
                    self.moveRight(env)
                elif(x1 < x0):
                    self.moveLeft(env)
                else:
                    return
#:::::Search Algorithms:::::
    def DFS(self,env):
        #reset stack
        self.list = [0]
        self.visited = []
        self.stepCount = 0
        while (len(self.list) > 0):
            parent = self.list.pop();
            log("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                log("found path to goal")
                #self.finalPath = self.trimPath(env)
                return (1,self.stepCount)
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.list:
                    self.list.append(item)
                    self.pathRecord.append((parent,item))
                    self.stepCount += 1
                    log("added Square:{0}: to stack, stack is now {1}".format(item,self.list))
            self.visited.append(parent)
        return (0, -1)
    def BFS(self,env):
        #reset queue
        self.list = [0]
        self.visited = []
        self.pathRecord = [(0,0)]
        self. success = 0
        self.stepCount = 0
        while (len(self.list) > 0):
            parent = self.list.pop(0)
            log("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) == 3:
                log("found path to goal")
                log("Path record holds:{0}".format(self.pathRecord))
                #self.finalPath = self.trimPath(env)
                return (1, self.stepCount)
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.list:
                    self.list.append(item)
                    self.stepCount += 1
                    self.pathRecord.append((parent,item))
                    log("added Square:{0}: to Queue, Queue is now {1}".format(item,self.list))
            self.visited.append(parent)
        return (0,-1)
    def UCS(self,env):
        #reset queue
        self.list = [0]
        self.visited = []
        self.stepCount = 0
        while (len(self.list) > 0):
            log("current Queue {0}".format(self.list))
            parent = self.list.pop(0)
            log("parent is {0}".format(parent))
            log("parent[1] is {0}".format(parent[1]))
            if self.squareToNode(env,parent[1][len(parent[1])-1]) == 3:
                log("this is the path? {0}".format(parent[1]))
                self.finalPath = self.trimPath()
                log("{0}".format(self.finalPath))
                return (1,self.stepCount)
            for child in self.expand(env,parent[1][len(parent[1])-1]):
                if child in self.visited:
                    continue
                if child not in parent[1]:
                    log("adding Child:{0}: to parent".format(child))
                    temp = [parent[0]+1,(parent[1] + [child])]
                    log(" About to add temp = {0} to queue".format(temp))
                    self.list.append(temp)
                    self.pathRecord.append((parent,child))
                    self.list.sort()
                    log("element added is :{0}".format(temp))
            self.visited.append(parent)
        return (0, 0)
    def greedy(self,env):
        self.list = [0]
        self.visited = []
        self.stepCount = 0
        while len(self.list) > 0:
            parent = self.list.pop(0)
            log("    parent:{0}".format(parent))
            #base cases
            if self.squareToNode(env, int(parent)) == 3:
                log("SUCCESS: Path found!")
                return (1, self.stepCount)
            if parent in self.visited:
                log("FAILURE: stuck in loop")
                return (0,0)
            exp = self.expand(env,parent)
            choices = []
            for i in range(0,len(exp)):
                choice = (exp[i], self.findHyoo(env, exp[i]))
                log("adding choice: {0}".format(choice))
                choices.append(choice)
            choices.sort(key = operator.itemgetter(1))
            log("choices (sorted): {0}".format(choices))
            if len(choices) >0:
                currentTest = choices.pop(0)[0]
                self.list.append(currentTest)
                self.stepCount += 1
                self.pathRecord.append((parent,currentTest))
                log("Moving to {0}".format(currentTest))
                self.visited.append(parent)
            else:
                log("FAILURE, no available choices from this point")
                return (0,0)


    #def aStar(self,env):
    #    env.assignCosts()
    #    return
