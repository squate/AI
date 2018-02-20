#!/usr/bin/python3
#Nate Levy, Alan Sato, SCI326 hw2
from random import randint
from envi import *
import math
import queue
import random
import operator
import heapq

DEBUG = False
#:::::logger:::::
def log(s):
    if DEBUG == True:
        print(s)
def log2(s,e):
    if DEBUG == True:
        print(s,end = e)
def loge(s):
    if DEBUG == True:
        print(s)
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
    def setName (self,name):
        self.name = name
    def getName(self):
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
    def resetAttributes(self): #reset everythin but name
        self.visited = []
        self.stepCount = 0
        self.pathRecord = [(0,0)]
        self.finalPath = []
        self.locX = 0
        self.locY = 0
#:::::unit conversion (squares and nodes:::::
    def coordsToSquare(self,env,x,y): #coords go in, square index comes out
        return x * env.getSideLength() + y
    def squareToCoords(self, env, square): #square index in, coords out in a tuple
        x = int(square%env.getSideLength())
        y = int((square - x)/env.getSideLength())
        return (x,y)
    def squareToNode(self,env,square): #square index in, actual node returned
        l = env.getSideLength()
        x = int(square%l)
        y = int((square-x)/l)
        return env.nodes[x][y]
#:::::actuators (up, down, left and right):::::
    def moveUp(self,env): # +1 to y coordinate
        self.visit(env)
        log2("Moving UP        (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locY += 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def moveDown(self,env): # -1 to y coordinate
        self.visit(env)
        log2("Moving DOWN      (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locY -= 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def moveLeft(self,env): # -1 to x coordinate
        self.visit(env)
        log2("Moving LEFT      (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locX -= 1
        log("--> ("+ str(self.locX)+", "+str(self.locY)+")")
    def moveRight(self,env): # +1 to x coordinate
        self.visit(env)
        log2("Moving RIGHT     (" +str(self.locX)+", "+str(self.locY), ") ")
        self.locX += 1
        log("--> ("+str(self.locX)+", "+str(self.locY)+")")
    def visit(self,env): #mark a square on the environment as visited
        log("visiting ({0}, {1})".format(self.locX,self.locY))
        env.visit(self.locX,self.locY)
    def followPath(self,env): #physically move the agent along the path it found
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
#:::::Sensors::::::
    def expand(self,env,sqr): #input a square, returns array of its adjacent squares
        neighbors = []
        square = sqr
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                if self.squareToNode(env,i) != 1:
                    neighbors.append(i)
                #log(i)
        return neighbors
    def findHyoo(self,env,square): #Find Heuristic value for a square using distance formula
        x = int(square%env.sidelength)
        y = int((square-x)/env.sidelength)
        goalx = env.getSideLength()-1
        goaly = env.getSideLength()-1
        #distance formula
        d = ((((goalx-x)**2) + ((goaly-y)**2))**(1/2.0))
        log("distance from {0} to goal is {1}".format(square,d))
        return d
    def trimPath(self,env): #go through recorded path, streamline it
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
#:::::Search Algorithms:::::
    def DFS(self,env): #Depth-frist search pathfinding algorithm
        self.list =[0]
        self.resetAttributes() #list will be treated as a queue
        while (len(self.list) > 0): #while there are options to explore
            parent = self.list.pop(); #access top of stack
            log("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) == 3: #if we arrive at the exit
                log("found path to goal")
                #self.finalPath = self.trimPath(env) #follows a trimmed version of found path
                return (1,self.stepCount)
            for item in self.expand(env,parent): #expand parent node
                if item in self.visited: #if we already expanded this node
                    continue
                if item not in self.list: #add item to list
                    self.list.append(item)
                    self.pathRecord.append((parent,item))
                    self.stepCount += 1
                    log("added Square:{0}: to stack, stack is now {1}".format(item,self.list))
            self.visited.append(parent)
        return (0, -1) #if we run out of options and no path is found
    def BFS(self,env): #Breadth-first search pathfinding algorithm
        self.list = [0]
        self.resetAttributes() #list will be treated as a queue
        while (len(self.list) > 0):
            parent = self.list.pop(0) #access front of queue
            log("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) == 3: #if we're at the exit
                log("found path to goal")
                log("Path record holds:{0}".format(self.pathRecord)) #print path
                #self.finalPath = self.trimPath(env) #follows a trimmed version of found path
                return (1, self.stepCount)
            for item in self.expand(env,parent): #for child nodes
                if item in self.visited: #if we've already been to this node, don't do anything with it
                    continue
                if item not in self.list: #otherwise, add it to the back of the queue
                    self.list.append(item)
                    self.stepCount += 1
                    self.pathRecord.append((parent,item))
                    log("added Square:{0}: to Queue, Queue is now {1}".format(item,self.list))
            self.visited.append(parent)
        return (0,-1)
    def UCS(self,env):
        #reset queue
        self.list = [(0,[[0,0],])]
        self.visited = []
        self.stepCount = 0
        self.resetAttributes()
        while (len(self.list) > 0):
            log("current Queue {0}".format(self.list))
            parent = self.list.pop(0)
            log("parent is {0}".format(parent))
            log("parent[1][len(parent[1])-1][1] is {0}".format(parent[1][len(parent[1])-1][1]))
            if self.squareToNode(env,parent[1][len(parent[1])-1][1]) == 3:
                log("this is the path? {0}".format(parent[1]))
                self.pathRecord = parent[1]
                self.finalPath = self.trimPath(env)
                log("{0}".format(self.finalPath))
                return (1,parent[0])
            for child in self.expand(env,parent[1][len(parent[1])-1][1]):
                if child in self.visited:
                    continue
                if child not in parent[1]:
                    log("adding Child:{0}: to parent".format(child))
                    childnode = parent[1] + [[parent[1][len(parent[1])-1][1],child]]
                    log("this is the childnode {0}".format(childnode))
                    temp = [parent[0]+1,childnode]
                    self.list.append(temp)
                    self.list.sort(reverse = True)
                    log("element added is :{0}".format(temp))
            self.visited.append(parent[1][-1][1])
        return (0, 0)
    def greedy(self,env): #greedy pathfinding alg
        self.list = [0]
        self.resetAttributes()
        while len(self.list) > 0: #while there are options
            parent = self.list.pop(0) #get that item out of the thing
            log("    parent:{0}".format(parent))
            #base cases
            if self.squareToNode(env, int(parent)) == 3: #if we're at the exit
                log("SUCCESS: Path found!")
                return (1, self.stepCount)
            if parent in self.visited: #if we've already been here before
                log("FAILURE: stuck in loop")
                return (0,0)
            exp = self.expand(env,parent) #if base cases not met, expand parent node
            choices = []
            for i in range(0,len(exp)): #assign each child a heuristic value
                choice = (exp[i], self.findHyoo(env, exp[i]))
                choices.append(choice)
            choices.sort(key = operator.itemgetter(1)) #sort by distance, ascending
            log("     choices (sorted): {0}".format(choices))
            if len(choices) > 0: #if there are choices at all
                currentTest = choices.pop(0)[0]
                self.list.append(currentTest)
                self.stepCount += 1
                self.pathRecord.append((parent,currentTest))
                log("  Moving to {0}".format(currentTest))
                self.visited.append(parent)
            else: #if there are no options, additional base case
                log("FAILURE, no available choices from this point")
                return (0,0)
    def aStar(self,env):
        loge("A* is go")
        self.resetAttributes()
        self.list = PriorityQueue()
        self.list.put(0,0)
        costForNow = {}
        costForNow[0] = 0
        camefrom = {}
        camefrom[0] = None
        while len(self.list.elements) > 0:
            loge("    list as of now: {0}".format(self.list.elements))
            parent = int(self.list.get())
            #check to see if we made it
            if self.squareToNode(env, parent) == 3:
                loge("    SUCCESS! Path found! total cost: {0}\n".format(costForNow[parent]))
                return (1, self.stepCount,costForNow[parent])
            #expand current node
            loge("    checking square {}'s neighbors".format(parent))
            options = self.expand(env, parent)
            if len(options) > 0:
                loge("    options: {0}".format(options))
                for sqr in options:
                    newCost = costForNow[parent] + env.getCost(parent, int(sqr))
                    if sqr not in costForNow or newCost < costForNow[sqr]:#or self.squareToNode(env,sqr) == 3:
                        costForNow[sqr] = newCost
                        priority = newCost + self.findHyoo(env, sqr)
                        loge("    cost to move to {0}: {1}".format(sqr,priority))
                        self.list.put(sqr, priority)
                        self.stepCount += 1
                        camefrom[sqr] = parent
                        self.visited.append(parent)

        loge("    FAILURE: you done goofed\n")
        return (0,0)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self,item,priority):
        heapq.heappush(self.elements, (priority, item))
        loge("    pushing {0}".format(item))
    def get(self):
        return heapq.heappop(self.elements)[1]
