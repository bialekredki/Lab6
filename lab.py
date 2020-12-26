import numpy
import mazeutils
import bfs
import astar
import fmazereader
import sys
import time

MAZE = numpy.array([['#','#','#','O','O','O','#','#'],
                    ['#','O','O','O','#','O','#','#'],
                    ['#','O','#','#','#','O','#','#'],
                    ['O','O','O','O','#','G','#','#'],
                    ['O','#','#','#','#','O','#','#'],
                    ['O','#','#','O','O','O','#','#'],
                    ['O','#','#','O','#','#','#','#'],
                    ['S','O','O','O','#','#','#','#']])


                    


def solve_maze(method='bfs'):
    mazes = fmazereader.read_mazes()
    for m in mazes:
        if m is None:
            continue
        print("Original : ",'\n',m)
        start, goal = mazeutils.scan(m)
        graph = mazeutils.convert_maze_to_graph(m)
        path_bfs = bfs.bfs(graph,start,goal)
        solved_bfs = mazeutils.mark_path(m, path_bfs)
        path_astar = astar.search(graph,start,goal,1)
        solved_astar = mazeutils.mark_path(m, path_astar)
        for x in range(3):
            print('\n')
        print("Solved using Breadth-First-Search : ",'\n',solved_bfs)
        print("\n\nSolved using A* algorithm :",'\n', solved_astar)

if __name__ == '__main__':
    solve_maze()