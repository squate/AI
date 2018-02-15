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
        #self.adj = []
        self.queue = []
        self.stack = []
        self.visited = []
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
    def setSquare(self,env):
        self.square = self.locX * env.getSideLength() + self.locY()
    def nodeToSquare(self,env,x,y):
        return x * env.getSideLength() + y
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
        adjacent = []
        square = self.locX * env.getSideLength() + self.locY
        for i in range(0,env.getSideLength()*env.getSideLength()):
            if env.edges[square][i] == 1:
                if self.squareToNode(env,i) != 1:
                    adjacent.append(i)
        return adjacent
    #Probably only need expand or getAdjacencies but we can do this later
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

    def trimPath(self,env):
        temp = []
        goal = self.pathRecord.pop()
        while goal[1]!=((env.getSideLength()**2)-1):
            goal = self.pathRecord.pop()
        print("Goal is {0}, and we got there from {1}".format(goal[1],goal[0]))
        temp.append(goal)
        while temp[0][0] != 0:
            for item in self.pathRecord:
                if item[1] == temp[0][0]:
                    temp.insert(0,item)
        print("this is the trimmed path{0}".format(temp))
        return temp
#:::::Search Algorithms:::::
    def DFS(self,env):
        #reset stack
        self.stack = [0]
        self.visited = []
#        self.stack += self.getAdjacencies(env) #push onto stack the squares that you can move to from origin
        while (len(self.stack) > 0):
            parent = self.stack.pop();
            print("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                self.trimPath(env)
                return True
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.stack:
                    self.stack.append(item)
                    self.pathRecord.append((parent,item))
                    #if self.squareToNode(env,item) ==1:
                    #    print("about to add an item, taken from expand that is a wall")
                    print("added Square:{0}: to stack, stack is now {1}".format(item,self.stack))
            self.visited.append(parent) 
    def BFS(self,env):
        #reset queue
        self.queue = [0]
        self.visited = []
        self.pathRecord = [(0,0)]
        #self.queue += self.getAdjacencies(env)        
        while (len(self.queue) > 0):
            parent = self.queue.pop(0)
            print("Parent = {0}".format(parent))
            if self.squareToNode(env,parent) ==3:
                print("found path to goal")
                print("Path record holds:{0}".format(self.pathRecord))
                self.trimPath(env)
                return True
            for item in self.expand(env,parent):
                if item in self.visited:
                    continue
                if item not in self.queue:
                    self.queue.append(item)
                    self.pathRecord.append((parent,item))
                    print("added Square:{0}: to Queue, Queue is now {1}".format(item,self.queue))
            self.visited.append(parent)
    def UCS(self,env):
        self.queue = [[0,[0,]]]
        self.visited =[]
        while (len(self.queue) > 0):
            print("current Queue {0}".format(self.queue))
            parent = self.queue.pop(0)
            print("parent is {0}".format(parent))
            print("parent[1] is {0}".format(parent[1]))
            if self.squareToNode(env,parent[1][len(parent[1])-1])==3:
                print("this is the path? {0}".format(parent[1]))
                return parent
            for child in self.expand(env,parent[1][len(parent[1])-1]):
                if child in self.visited:
                    continue
                if child not in parent[1]:
                    print("adding Child:{0}: to parent".format(child))
                    temp = [parent[0]+1,(parent[1] + [child])]
                    print(" About to add temp = {0} to queue".format(temp))
                    self.queue.append(temp)
                    self.queue.sort()
                    print("element added is :{0}".format(temp))
            self.visited.append(parent) 
        return
    def greed(self,env):
        return
    def aStar(self,env):
        return
