from Queue import Queue
from Stack import Stack

class Graph:
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        self.nodes.add(node)

    def set_all_nodes_unvisited(self):
        for node in self.nodes:
            node.set_visited(False)

    def get_size(self):
        return len(self.nodes)

    def depth_first_search(self, source, target):
        stack = Stack()
        found = None

        self.set_all_nodes_unvisited()
        stack.empty()
        stack.push(source)

        while not stack.is_empty():
            current_node = stack.pop()

            if current_node.is_visited():
                continue

            if current_node.data == target:
                return target

            current_node.set_visited(True)

            for adjacent_node in current_node.get_edges():
                if not adjacent_node.is_visited():
                    stack.push(adjacent_node)

        return found

    def breadth_first_search(self, source, target):
        queue = Queue()
        found = None

        self.set_all_nodes_unvisited()
        queue.empty()
        queue.add(source)

        while not queue.is_empty():
            current_node = queue.poll()

            if current_node.is_visited():
                continue

            if current_node.data == target:
                return target

            current_node.set_visited(True)

            for adjacent_node in current_node.get_adjacent_nodes():
                if not adjacent_node.is_visited():
                    queue.add(adjacent_node)

        return found

    # BFS from each node to print all connections
    def __str__(self):
        queue = Queue()
        graph_string = ""

        for node in self.nodes:
            self.set_all_nodes_unvisited()
            queue.empty()
            queue.add(node)
            node_string = ""

            while not queue.is_empty():
                current_node = queue.poll()

                if current_node.is_visited():
                    continue

                current_node.set_visited(True)
                node_string += str(current_node) + " -> "

                for adjacent_node in current_node.get_edges():
                    if not adjacent_node.is_visited():
                        queue.add(adjacent_node)

            if node_string != "":
                graph_string += node_string[:-4] + "\n"

        return graph_string


class Node:
    def __init__(self, data):
        self.adjacent_nodes = set()
        self.data = data
        self.visited = False
        self.active = False

    def set_visited(self, visited):
        self.visited = visited

    def is_visited(self):
        return self.visited

    def add_adjacent_node(self, node):
        self.adjacent_nodes.add(node)

    def get_adjacent_nodes(self):
        return self.adjacent_nodes

    def __str__(self):
        return "[%s]" % self.data