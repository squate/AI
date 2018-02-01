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
    dungeon = envi()
    dungeon.addWalls()
    dungeon.showgrid()
