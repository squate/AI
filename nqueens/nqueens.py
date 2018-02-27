#!/usr/bin/python3
# Nate Levy, Alan Sato
# n-queens problem

import random
DEBUG = True

def log(n):
    if DEBUG == True:
        print n

class Env():
    def __init__(self):
        self.size = 4
        self.queens = self.makeColumns(self)
        self.totalDanger = self.detectDanger(self)

    def makeColumns(self,n):
        col = list()
        for i in range(self.size-1):
            col.append((random.randint(0,self.size-1),0))
        return col

    def detectDanger(self):
        self.resetDanger()
        for i in range(self.size - 1):
            for j in range(i+1, self.size-1):
                #if on same row as other
                if self.queens[i] == self.queens[j]:
                    self.noteDanger(i, j)
                #if same up-right diagonal from queens[i]
                if self.queens[i] = (self.queens[j] + (j-i)):
                    self.noteDanger(i, j)
                #same down-right diagonal from queens[i]
                if self.queens[i] = (self.queens[j] + (i-j)):
                    self.noteDanger(i, j)

    def resetDanger(self):
        self.totalDanger = 0
        for i in range(self.n-1)
            self.queens[i][0] = 0

    def noteDanger(self, i, j):
        self.totalDanger += 1
        self.queens[i][1] += 1
        self.queens[j][1] += 1
