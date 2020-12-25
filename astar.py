"""
    ASTAR_PY_
    A* Algorithm for maze-solving.
    Contents:
    Node(Class)
    search
    build_path
    AUTHOR OSKAR KORGUL
"""
class Node:
    """
    Class used to store information about any state in the search space. It stores information about:
        parent:Node -> the previously considered Node(ie position)
        position:Tuple -> coordinates of this Node. Can be treated as it's unique ID.
        g:double -> The exact cost of moving from starting-node to this node
        h:double -> The estimated cost of moving from this node to the end-node
        f:double -> The sum of two previously mentioned costs
    """
    def __init__(self, parent=None, position:tuple=None):
        self.parent = parent
        self.position = position
        
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self,x):
        return self.position == x.position

def search(graph,start,end,cost):
    """

    :param graph:
    :param start:
    :param end:
    :param cost:
    :return:
    """
    # Create starting-node and end-Node
    start_node =  Node(None, start)
    end_node = Node(None, end)
    visited = []
    queue = []
    queue.append(start_node)
    while len(queue) > 0:
        current_node = queue[0]
        current_index = 0

        for index, item in enumerate(queue):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        queue.pop(current_index)
        visited.append(current_node)
        if current_node == end_node:
            return build_path(current_node)
        children = []
        for child in graph[current_node.position]:
            new_node = Node(current_node, child)
            children.append(new_node)

        for child in children:
            if child in visited:
                continue
            child.g = current_node.g + cost
            child.h = (child.position[0] - end_node.position[0])**2 + (child.position[1] - end_node.position[1])**2
            child.f = child.g + child.h
            if len([i for i in queue if child == i and child.g > i.g]) > 0:
                continue
            queue.append(child)

def build_path(node):
    path = []
    current = node
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    del path[0]
    return path