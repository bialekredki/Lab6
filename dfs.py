"""
    DFS_PY_
    DFS Algorithm for maze solving
    AUTHOR OSKAR KORGUL
"""
import mazeutils

def dfs(maze:dict,start:tuple,goal:tuple):
    # Create visited,queue and waiting lists/dictionary
    visited = dict()
    queue = list()
    waiting = list()
    # Append starting position to visited and queue
    queue.append(start)
    visited[start] = None
    # Set previous as start for the first position after starting position
    previous = start
    # Repeat while queue is full
    while len(queue) > 0 :
        # Take the first element from queue
        current = queue[0]
        mazeutils.dequeue(queue, 0)
        # If in not starting position add current to visited
        if current != start:
            visited[current] = previous
        # If found goal return visited graph
        if goal in maze[current]:
            visited[goal] = current
            return visited
        isFirst = True
        # If current position is not a dead end
        if len(maze[current]) >= 1 and len([i for i in maze[current] if i in visited]) != len(maze[current]):
            # Add the first child to queue
            for index,child in enumerate(maze[current]):
                if isFirst and child not in visited:
                    queue.append(child)
                    previous = current
                    isFirst = False
                # Add other children to waiting list
                elif child not in visited and not isFirst:
                    waiting.append((current,child))
        # If dead end take the latest position from waiting list and add it to queue
        else:
            last_waiting = waiting[-1]
            queue.append(last_waiting[1])
            previous = last_waiting[0]
            mazeutils.dequeue(waiting, -1)
    return None




