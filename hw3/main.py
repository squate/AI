#! /usr/bin/python3
#import everything
#Nate Levy, Alan Sato, SCI326 hw2
from envi import *
from agent import *
import queue
DEBUG = True
#:::::logger:::::
def log(s):
    if DEBUG == True:
        print(s)
def log2(s,e):
    if DEBUG == True:
        print(s,end = e)
#:::::non-meta functions:::::
def main():
    dungeon = envi(6)
    bruce = Agent()
    totalGreed = 0
    finalTest(bruce,dungeon,100)

def finalTest(agent,environment,reps):
    totalBFS = 0
    totalDFS = 0
    totalUCS = 0
    totalGreedy = 0
    totalFail = 0
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.BFS(dungeon)
        if run[0] == 1:
            totalBFS += run[1]
        elif run[0] == 0:
            totalFail += 1
    avg = totalBFS / (reps - totalFail)
    log("Avg Steps/ successful run (BFS): {0}".format(avg))
    log("Percent successful runs (BFS): {0}\n".format((((reps-totalFail)/reps))*100))
    totalFail = 0

    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.DFS(dungeon)
        if run[0] == 1:
            totalDFS += run[1]
        elif run[0] == 0:
            totalFail += 1
    avg = (totalDFS / (reps - totalFail))
    log("Avg Steps/ successful run (DFS): {0}".format(avg))
    log("Percent successful runs (DFS): {0} \n".format((((reps-totalFail)/reps))*100))
    toalFail = 0

    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.greedy(dungeon)
        if run[0] == 1:
            totalGreedy += run[1]
        elif run[0] == 0:
            totalFail += 1
    avg = totalGreedy / (reps - totalFail)
    log("Avg Steps/ successful run (Greedy): {0}".format(avg))
    log("Percent successful runs (Greedy): {0}\n".format((((reps-totalFail)/reps))*100))
    total= 0

    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.UCS(dungeon)
        if run[0] == 1:
            totalUCS += run[1]
        else:
            totalFail += 1
    avg = totalUCS / (reps - totalFail)
    print("Avg Steps/ successful run (UCS): {0}".format(avg))
    print("Percent successful runs (UCS): {0}\n".format((reps-totalFail)/reps)*100)


main()
