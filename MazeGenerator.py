import argparse
import os
import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
from errno import EEXIST
from os import makedirs, path

def maze(width=50, height=50, complexity=0.75, density=1.00):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1]))) # number of components
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2))) # size of components
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2 # pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z

def mkdir_p(mypath):
    '''Creates a directory. equivalent to using mkdir -p on the command line'''
    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise


def generate_data(size=4):
    try:
        for i in range(0 ,int(size)):
            pyplot.figure(figsize=(10, 5))
            pyplot.imshow(maze(80, 40), cmap=pyplot.cm.binary, interpolation='nearest')
            pyplot.xticks([]), pyplot.yticks([])
            pyplot.savefig("/Users/bmathew2014/PycharmProjects/MazePathFinder/Assets/"+str(i)+'.png')

    except Exception as e:
        print(str(e))

def main():
    parser = argparse.ArgumentParser(description="Maze Generation Script-Script")
    parser.add_argument("-n", metavar='N',type=int,help="Sample Input Size")
    parser.add_argument("-s", metavar='S',type=bool,help="Show Random Images")
    args = parser.parse_args()
    # If Assesst Folder does not Exist then create it

    if(os.path.isdir("/MazePathFinder/Assets/")):
        os.makedirs("/MazePathFinder/Assets/")

    else:
        generate_data(args.n)

    if(args.s):
        print("Displaying Images:\n")
        pyplot.show()


if __name__=='__main__':
    main()