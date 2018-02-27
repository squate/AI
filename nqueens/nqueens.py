#!/usr/bin/python3
# Nate Levy, Alan Sato
# n-queens problem

import random

class Env():
    def __init__(self):
        self.n = 4
        self.columns = self.makeColumns(self, self.n)
        self.queensInDanger = self.detectDanger(self)

    def makeColumns(self,n):
        col = list()
        for i in range(n-1):
            col.append(random.randint(0,n-1))
        return col

    def detectDanger(self):
        totalDanger = 0
        for each in self.columns:
