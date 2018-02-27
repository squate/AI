#!/usr/bin/python3
# Nate Levy, Alan Sato
# n-queens problem

import random
DEBUG = True

def log(n):
    if DEBUG == True:
        print(n)

class Env():

    def __init__(self):
        self.size = 4
        self.queens = self.makeColumns(self.size)
        self.totalDanger = self.detectDanger()

    def makeColumns(self,n):
        col = list()
        for i in range(n):
            col.append([random.randint(0,self.size-1),0])
        return col

    def detectDanger(self):
        self.resetDanger()
        for i in range(self.size):
            for j in range(i+1, self.size):
                #if on same row as other
                if self.queens[i][0] == self.queens[j][0]:
                    self.noteDanger(i, j)
                #if same up-right diagonal from queens[i]
                if self.queens[i][0] == (self.queens[j][0] + (j-i)):
                    self.noteDanger(i, j)
                #same down-right diagonal from queens[i]
                if self.queens[i][0] == (self.queens[j][0] + (i-j)):
                    self.noteDanger(i, j)

    def resetDanger(self):
        self.totalDanger = 0
        for i in range(self.size-1):
            self.queens[i][1] = 0
    def noteDanger(self, i, j):
        self.totalDanger += 1
        self.queens[i][1] += 1
        self.queens[j][1] += 1


#Display Purposes
    def showcol(self):
        print("this is what the list looks like (row of queen, number of collisions):")
        print("{0}".format(self.queens))
        print("this is what the grid would look like based on the list")
        grid = [[] for i in range(self.size)]
        for j in range(self.size):
            for i in range(self.size):
                if self.queens[i][0] == j : 
                    grid[j].append("X")
                else:
                    grid[j].append("o")
        for k in range(self.size):
            print("{}".format(grid[k]))

# Run the Juuls
def main():
    place = Env()
    place.showcol()
main()
