"""
    ASTAR_PY_
    A* Algorithm for maze-solving.
    Contents:
    Node(Class)
    search
    build_path
    AUTHOR OSKAR KORGUL
"""

import bfs


class Node:
    """
    Class used to store information about any state in the search space. It stores information about:
        parent:Node -> the previously considered Node(ie position)
        position:Tuple -> coordinates of this Node. Can be treated as it's unique ID.
        g:double -> The exact cost of moving from starting-node to this node
        h:double -> The estimated cost of moving from this node to the end-node
        f:double -> The sum of two previously mentioned costs
    """

    def __init__(self, parent=None, position: tuple = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, x):
        return self.position == x.position


def search(graph: dict, start: tuple, end: tuple, cost: float):
    """
    Uses A* algorithm to find path from starting-node to end-node.
    :param graph:Dictionary. Graph representation of a maze.
    :param start:Tuple. Starting-node position.
    :param end:Tuple. Ending-node position.
    :param cost: Cost of movement between two nodes.
    :return:Returns path from starting node to end-node.
    """
    # Create starting-node and end-Node
    start_node = Node(None, start)
    end_node = Node(None, end)
    # Create visited list and queue list for storing visited and yet-to-be-visited nodes
    visited = []
    queue = []
    # Append starting node to the queue
    queue.append(start_node)
    # Start of the actual algorithm. Perform until there's nothing in the queue.
    while len(queue) > 0:
        # Take the first node from the queue
        current_node = queue[0]
        current_index = 0
        # If there's a node with lower cost than current node's cost in the queue switch to this one.
        for index, item in enumerate(queue):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # Take current node out of queue
        bfs.dequeue(queue, current_index)
        # Add this to visited list
        visited.append(current_node)
        # If current_node is end-node then return the path
        if current_node == end_node:
            return build_path(current_node)
        # Look for current node's children in graph.
        children = []
        for child in graph[current_node.position]:
            new_node = Node(current_node, child)
            children.append(new_node)
        # Calculate estimated cost for node's children.
        for child in children:
            if child in visited:
                continue
            child.g = current_node.g + cost
            child.h = (child.position[0] - end_node.position[0]) ** 2 + (child.position[1] - end_node.position[1]) ** 2
            child.f = child.g + child.h
            if len([i for i in queue if child == i and child.g > i.g]) > 0:
                continue
            queue.append(child)


def build_path(node: Node):
    """
    Builds path using Node class. Goes up using information about parent.
    :param node: Ending node.
    :return: Returns list of consecutive nodes' positions.
    """
    path = []
    current = node
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    bfs.dequeue(path, 0)
    return path
