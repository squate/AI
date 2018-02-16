#! /usr/bin/python3
#import everything
#Nate Levy, Alan Sato, SCI326 hw2
from envi import *
from agent import *
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
    finalTest(bruce, dungeon, 100)

def finalTest(agent,environment,reps):
    totalBFS = 0
    totalDFS = 0
    totalUCS = 0
    print("testing...")
    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        agent.BFS(environment)
        agent.followPath(environment)
        totalBFS += agent.getstepCount()
    avgBFS = totalBFS / reps
    print("Avg Steps/ run (BFS): {0}".format(avgBFS))

    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        agent.DFS(environment)
        agent.followPath(environment)
        totalDFS += agent.getstepCount()
    avgDFS = totalDFS / reps
    print("Avg Steps/ run (DFS): {0}".format(avgDFS))

    for i in range(reps):
        dungeon = envi(environment.getSideLength())
        agent.UCS(environment)
        agent.followPath(environment)
        totalUCS += agent.getstepCount()
    avgUCS = totalUCS / reps
    print("Avg Steps/ run (UCS): {0}".format(avgUCS))

main()
