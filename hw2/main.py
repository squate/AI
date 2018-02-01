#Nate Levy, Alan Sato, SCI326 hw2
#! /usr/bin/python3
#import everything
from envi import *
from agent import *
DEBUG = False
#:::::logger:::::
def log(s):
    if DEBUG == True:
        print(s)
def log2(s,e):
    if DEBUG == True:
        print(s,end = e)
def main():
    env = envi()
    log("making dirty")
    env.superdirty()
    log("Number of Dirty places: {0}".format(env.dirtynum))
    romb = Agent()
    env.showgrid(romb)
    romb.assumeThePosition(env)
    d = env.dirtleft()
    while d != 0: #action loop
        romb.think(env)
        d = env.dirtleft()
    env.showgrid(romb)
    return env.evaluate(romb)

total = 0
reps = 10000
max = 0;
min = 2;
for i in range(0,reps-1):
    s = main()
    if s < min:
        min = s
    if s > max:
        max = s
    total += s
avgScore = total/reps
print("reps: "+str(reps)+", avg: "+ str('{0:.3g}'.format(avgScore)) + ", worst score: "+str(max)+", best score: "+str(min))
