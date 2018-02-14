#! /usr/bin/python3
#import everything
#Nate Levy, Alan Sato, SCI326 hw2
from envi import *
from agent import *
#DEBUG = False
#:::::logger:::::
#def log(s):
#    if DEBUG == True:
#        print(s)
#def log2(s,e):
#    if DEBUG == True:
#        print(s,end = e)

def main():
    dungeon = envi(6)
    dungeon.addWalls()
    bruce = Agent()
    dungeon.showgrid(bruce)
#    bruce.findHyoo(dungeon,0,0) Testing to see if Heuristic value works
#    bruce.findHyoo(dungeon,1,0)
#    bruce.findHyoo(dungeon,0,1)
#    dungeon.showedges()
#    bruce.DFS(dungeon)
#    dungeon.showgrid(bruce)
main()
