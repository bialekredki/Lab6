"""
    DFS_PY_

    AUTHOR OSKAR KORGUL
"""
import bfs

def dfs(maze:dict,start:tuple,goal:tuple):
    visited = dict()
    queue = list()
    waiting = list()
    queue.append(start)
    visited[start] = None
    previous = start
    while len(queue) > 0 or len(waiting) > 0:
        current = queue[0]
        bfs.dequeue(queue,0)
        if current != start:
            visited[current] = previous
        if goal in maze[current]:
            visited[goal] = current
            return visited
        isFirst = True
        if len(maze[current]) >= 1 and len([i for i in maze[current] if i in visited]) != len(maze[current]):
            for index,child in enumerate(maze[current]):
                if isFirst and child not in visited:
                    queue.append(child)
                    previous = current
                    isFirst = False
                elif child not in visited and not isFirst:
                    waiting.append((current,child))
        else:
            last_waiting = waiting[-1]
            queue.append(last_waiting[1])
            previous = last_waiting[0]
            bfs.dequeue(waiting,-1)
    return None




