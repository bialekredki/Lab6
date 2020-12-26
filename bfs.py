"""
    BFS_PY_
    BREADTH FIRST SEARCH ALGORITHM
    contents:
    bfs
    backtrack
    AUTHOR OSKAR KORGUL
"""

def bfs(graph:dict,start:tuple,goal:tuple,visited:dict=None,queue:list=None):
    """
    BFS algorithm for solving maze
    :param graph:Dictionary. Graphs for of the maze.
    :param start:Tuple. Start-point coordinates.
    :param goal:Tuple. End-point coordinates.
    :param visited:Dictionary. Represents connections between visited nodes. Set to NONE as default.
    :param queue:List. For yet-to-be-visited tiles. Set to NONE as default.
    :return:Uses recursion. Returns path obtained using BFS algorithm on first-layer of recursion.
    """
    if visited is None or queue is None:
        visited = {}
        queue = [start]
    current = queue[0]
    dequeue(queue,0)
    if len(visited) == 0:
        visited[current] = None
    for n in graph[current]:
        if n in visited:
            visited[current] = n
    if goal in graph[current]:
        visited[goal] = current
        return
    for n in graph[current]:
        if n not in visited:
            queue.append(n)
    bfs(graph,start,goal,visited,queue)
    if current == start:
        return backtrack(visited,start,goal)

    
def backtrack(graph:dict,start:tuple,goal:tuple):
    """
    Creates path from given graph of connections between visited nodes.
    :param graph: Dictionary.
    :param start: Tuple. Start-point position.
    :param goal: Tuple. End-point position.
    :return: List. Path from starting-point to the end-point.
    """
    path = []
    while True:
        path.append(goal)
        goal = graph[goal]
        if goal == start:
            break
    del path[0]
    return path
