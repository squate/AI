#! /usr/bin/python3
#import everything
#Nate Levy, Alan Sato, SCI326 hw2
from envi import *
from agent import *
import queue
DEBUG = True
#:::::loggers:::::
def log(s):
    if DEBUG == True:
        print(s)
#:::::non-meta functions:::::
def main():
    dungeon = envi(6)
    bruce = Agent()
    totalGreed = 0

    finalTest(bruce,dungeon,1000)

def finalTest(agent,environment,reps):
    totalBFS = 0
    totalDFS = 0
    totalUCS = 0
    totalGreedy = 0
    totalFail = 0

    print("BFS:")
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.BFS(dungeon)
        if run[0] == 1:
            totalBFS += run[1]
        elif run[0] == 0:
            totalFail += 1
    if (totalFail<reps):
        avg = totalBFS / (reps - totalFail)
        odds = 100*(reps-totalFail)/reps
        print("    Avg Steps to exit: {0}".format(avg))
        print("    Percent success: {0}\n".format(odds))
    else:
        print("    Failed every one of its {0} runs\n".format(reps))

    totalFail = 0

    print("DFS:")
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.DFS(dungeon)
        if run[0] == 1:
            totalDFS += run[1]
        elif run[0] == 0:
            totalFail += 1
    if (totalFail<reps):
        avg = totalDFS / (reps - totalFail)
        odds = 100*(reps-totalFail)/reps
        print("    Avg Steps to exit: {0}".format(avg))
        print("    Percent success: {0}\n".format(odds))
    else:
        print("    Failed every one of its {0} runs".format(reps))

    totalFail = 0

    print("Greedy:")
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.greedy(dungeon)
        if run[0] == 1:
            totalGreedy += run[1]
        elif run[0] == 0:
            totalFail += 1
    if (totalFail < reps):
        avg = totalGreedy / (reps - totalFail)
        odds = 100*(reps-totalFail)/reps
        print("    Avg Steps to exit: {0}".format(avg))
        print("    Percent success: {0}\n".format(odds))
    else:
        print("    Failed every one of its {0} runs".format(reps))
        print("{0}".format(totalFail))

    totalFail = 0

    print("UCS:")
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        run = agent.UCS(dungeon)
        if run[0] == 1:
            totalUCS += run[1]
        else:
            totalFail += 1
    if (totalFail<reps):
        avg = totalUCS / (reps - totalFail)
        odds = 100*(reps-totalFail)/reps
        print("    Avg Steps to exit: {0}".format(avg))
        print("    Percent success: {0}\n".format(odds))
    else:
        print("    Failed every one of its {0} runs".format(reps))


main()
