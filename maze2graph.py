"""
    MAZE_2_GRAPH_PY_
    Convert maze(numpy's array) to Python's dictionary(graph) and other operations.
    Contents:
    convert_maze_to_graph
    mark_path
    scan
    look_for_neighbours
    fits_in_boundaries
    AUTHOR OSKAR KORGUL
"""
import numpy
import copy

def convert_maze_to_graph(maze:numpy.array):
    """
    Converts maze(numpy's array) to dictionary where every passable tile stores information about its neighbours.
    :param maze: Maze to be converted
    :return: Returns graph representation of maze
    """
    shape = maze.shape
    graph = {}
    for x in range(shape[0]):
        for y in range(shape[1]):
            if maze[x,y] != '#':
                neighbours = look_for_neighbours(maze,(x,y))
                if neighbours != -1:
                    graph[(x,y)] = neighbours
                        
    return graph

def mark_path(maze:numpy.array, path):
    """
    Marks path onto maze in its array form. Doesn't change the maze parameter.
    :param maze: Numpy's array
    :param path: Dictionary obtained using BFS/A* Algorithm
    :return:Returns maze with a path from start to the end
    """
    it = 0
    maze_copy = copy.deepcopy(maze)
    for p in path:
        if len(path) - it % 10 == 0:
            it = 10
        maze_copy[p] = str(len(path) - it)
        it = it + 1
    return maze_copy
            
    
  
def scan(maze:numpy.array):
    """
    Scans maze for both start-point and end-point.
    :param maze: Numpy's array
    :return: Returns two tuples(positions) of both start-point and end-point. Throws exception if it can't find any of them.
    """
    shape = maze.shape
    print("shape ",shape[0],'\t',shape[1])
    goal = None
    start = None
    for x in range(shape[0]):
        for y in range(shape[1]):
            if maze[x,y] == 'G':
                goal = (x,y)
            elif maze[x,y] == 'S':
                start = (x,y)
        if goal is not None and start is not None:
            return start,goal
    raise Exception("Maze lacks start and/or goal")
    
def look_for_neighbours(maze:numpy.array, position:tuple):
    """
    Search for neighbours of maze's tile.
    :param maze: Numpy's array
    :param position: A tuple. Position of tile.
    :return: Return list of postitions of all neighbouring, passable tiles of the first tile
    """
    position_change = (-1,1)
    shape = maze.shape
    result = []
    for pos_ch in position_change:
        horizontal = (position[0],position[1]+pos_ch)
        vertical = (position[0]+pos_ch,position[1])
        if fits_in_boundaries(shape[0],vertical[0]) and maze[vertical] != '#':  
            result.append(vertical)
        if fits_in_boundaries(shape[1], horizontal[1]) and maze[horizontal] != '#':
            result.append(horizontal)
    if len(result) == 0:
        return -1
    return result
        
        
        
def fits_in_boundaries(size:int,position:int):
    """
    Check whether given postion fits into size of maze(ie an algorithm won't be looking outside maze's boundaries).
    :param size: Horizontal/vertical size. Number of columns/rows.
    :param position: Position for which we check boundary condition.
    :return: Boolean value. True if it fits, false if it doesn't.
    """
    return position >= 0 and position < size

        