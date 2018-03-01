#!/usr/bin/python3
# Nate Levy, Alan Sato
# n-queens problem
import copy
import random
DEBUG = False

def log(n):
    if DEBUG == True:
        print(n)

#Class Env will be a n x n "grid"
#The problem can only have one queen per column, so we will represent the grid as a single "flat" list
# like [0,1,2,3] where the numbers each represent the queen's position in that column
#The variable totalDanger will keep track of if a win condition has been met


class Env():
    #initialization
    def __init__(self,big):
        self.size = big
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
        #log("total danger for this configuration= {0}".format(danger))
        return danger
    def resetDanger(self,queens):
        for i in range(self.size):
            queens[i][1] = 0
    def noteDanger(self, i, j,queens):
        queens[i][1] += 1
        queens[j][1] += 1

    #Solutions:
    
    #solve will take the most contraining element, try to change it such that the next iteration has less conflicts
    #can get stuck if changing the most contraining would only result in a worse total value
    def solve(self):
        queens = self.columns #Here I make another pointer to self.columns so that we dont have to type self.columns everywhere
        while self.totalDanger > 0: 
            #This part will find the most constraining node's index
            mostConing = queens.index(max(queens,key = lambda item:item[1]))#finding the most constraining by the second element in the tuple (which is a list)
            log("current configuration: {0}".format(queens))
            log("The index of the most constraining variable is: {0}".format(mostConing))
        
            #Here I create the variables nextBest and nextBestConfig
            #NextBest is the amount of violations the "next best" configuration has
            #the nextBestConfig records the number row the queen in question ("the most constraining queen") in the "next best" configuration
            nextBest = self.totalDanger
            nextBestConfig = queens[mostConing][0]

               
            for i in range(self.size):
                #Here i make a copy of queens, and change the row of the most constraining queen to i
                copyQueens = list(queens)
                copyQueens[mostConing][0]=i
                #dont forget to detectDanger such that copyQueens has updated violation information
                configDanger = self.detectDanger(copyQueens)
                log("new configuration possibility:{0}".format(copyQueens))
                #if the configuration has less violations than the current standing next best, log this configuration's danger and queen's row
                if configDanger<nextBest:
                    nextBest = configDanger
                    log("This is the nextBest config at  {0} ( supposed to be {0}) violations".format(nextBest,configDanger))
                    nextBestConfig = i
            #Once it checks every possibility for the queen
            #if there was a nextBest then change the current to the next best
            if nextBest<self.totalDanger:
                log("Changing to config {0} with the danger of {1} which is better than {2}".format(nextBestConfig,nextBest,self.totalDanger))
                self.columns[mostConing][0]=nextBestConfig
                self.totalDanger=self.detectDanger(queens)
                log(queens)
                self.showcol()
            else:
                break
        #once the loop ends, if your total danger was 0 you succeeded. If not...
        if self.totalDanger == 0:
            log("Success")
            log("final config:")
            self.showcol()
            return 1
        else:
            log("failure")
            return 0
    #
    #Display Purposes
    #does not need to be passed the columns cus it doesn't need to be multi-use

    def showcol(self):
        log("this is what the list looks like (row of queen, number of collisions):")
        log("{0}".format(self.columns))
        log("this is what the grid would look like based on the list")
        grid = [[] for i in range(self.size)]
        for j in range(self.size):
            for i in range(self.size):
                if self.columns[i][0] == j : 
                    grid[j].append("X")
                else:
                    grid[j].append("o")
        for k in range(self.size):
            log("{0}".format(grid[k]))

#tests
def solvetest(runs,size):
    succ = 0
    for i in range(runs):
        place = Env(size)
        x = place.solve()
        if x == 1:
            succ +=1
    print("solve got {0}/{1}".format(succ,runs))
# Run the Juuls

def main():
    solvetest(1000,4)
main()
