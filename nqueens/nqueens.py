#!/usr/bin/python3
# Nate Levy, Alan Sato
# n-queens problem

import random
DEBUG = True

def log(n):
    if DEBUG == True:
        print(n)

#Class Env will be a n x n "grid"
#The problem can only have one queen per column, so we will represent the grid as a single "flat" list
# like [0,1,2,3] where the numbers each represent the queen's position in that column
#The variable totalDanger will keep track of if a win condition has been met


class Env():
    #initialization
    def __init__(self):
        self.size = 4
        self.columns = self.makeColumns(self.size)
        self.totalDanger = self.detectDanger(self.columns)
    def makeColumns(self,n):
        col = list()
        for i in range(n):
            col.append([random.randint(0,self.size-1),0])
        return col

    #"danger" detection

    def detectDanger(self,queens): #pass the queens over instead of directly manipulating such that we can pass "clones" of the list with alternate queen placement
        self.resetDanger(queens)
        danger = 0
        for i in range(self.size):
            for j in range(i+1, self.size):
                #if on same row as other
                if queens[i][0] == queens[j][0]:
                    danger += 1
                    self.noteDanger(i,j,queens)
                #if same up-right diagonal from queens[i]
                if queens[i][0] == (queens[j][0] + (j-i)):
                    danger += 1
                    self.noteDanger(i,j,queens)
                #same down-right diagonal from queens[i]
                if queens[i][0] == (queens[j][0] + (i-j)):
                    danger +=1
                    self.noteDanger(i,j,queens)
        print("total danger = {0}".format(danger))
        return danger
    def resetDanger(self,queens):
        for i in range(self.size-1):
            queens[i][1] = 0
    def noteDanger(self, i, j, queens):
        queens[i][1] += 1
        queens[j][1] += 1

    #Solutions:
    
    #BruteSolve will take the most contraining element, try to change it such that the next iteration has less conflicts
    #can get stuck if changing the most contraining would only result in a worse total value
    def bruteSolve(self,queens):
        #while self.totalDanger > 0:
        mostConing = queens.index(max(queens,key = lambda item:item[1]))
        log("The index of the most constraining variable is: {0}".format(mostConing))   
        #    for 
        return

    #Display Purposes
    #does not need to be passed the columns cus it doesn't need to be multi-use

    def showcol(self):
        print("this is what the list looks like (row of queen, number of collisions):")
        print("{0}".format(self.columns))
        print("this is what the grid would look like based on the list")
        grid = [[] for i in range(self.size)]
        for j in range(self.size):
            for i in range(self.size):
                if self.columns[i][0] == j : 
                    grid[j].append("X")
                else:
                    grid[j].append("o")
        for k in range(self.size):
            print("{}".format(grid[k]))

# Run the Juuls

def main():
    place = Env()
    place.showcol()
    place.bruteSolve(place.columns)
main()
