"""
    FMAZEREADER_PY_
    Maze File's Reader
    AUTHOR OSKAR KORGUL
    Reading mazes from text files.
    Maze has to be written in such way that walls are written using '#' sign, there has to be start-point and end point
    set with capital letters S and G respectively.
    Empty spaces can be noted using any other sign, however numbers are not recommended due to the fact that the path finding
    algorithms are going to use them for marking path on the maze.
    Mazes are required to have n-by-m shape.
    Look for STANDARD_88_1.MAZE file for the example.

"""
import numpy
import glob

def read_file(file):
    """
    Reads MAZE file.
    :param file:filename
    :return:Contents of file in form of string
    """
    f = open(file,'r')
    string = f.read()
    f.close()
    return string

def convert_to_array(maze):
    """
    Converts string contents of MAZE file into Numpy's array.
    :param maze: string
    :return:Numpy's array(maze)
    """
    columns = maze.find('\n')
    rows = maze.count('\n') + 1
    array = numpy.zeros((rows,columns), dtype=object)
    it = 0
    for x in range(rows):
        for y in range(columns):
            if maze[it] == '\n':
                it = it + 1
            if it >= len(maze):
                break
            array[x,y] = maze[it]
            it = it + 1
        if it >= len(maze):
            break
    return array



def is_correct(maze):
    """
    Check if the maze contains start-point and end-point.
    :param maze: string
    :return: Boolean value.
    """
    return 'G' in maze and 'S' in maze

def read_mazes():
    files = glob.glob("*.MAZE")
    mazes = []
    for f in files:
        string = read_file(f)
        if is_correct(string):
            mazes.append(convert_to_array(string))
        else:
            print("Cannot read : ", f)
    return mazes

def read_maze(filename):
    string = read_file(filename+".MAZE")
    return convert_to_array(string)

