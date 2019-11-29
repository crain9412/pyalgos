from Queue import Queue
from Stack import Stack
import sys

class WeightedUndirectedGraph:
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

            for adjacent_node in current_node.get_edges():
                if not adjacent_node.is_visited():
                    queue.add(adjacent_node)

        return found

    def dijkstras(self, source, target):
        for node in self.nodes:
            node.set_cost(sys.maxsize)
        queue = Queue()
        graph_string = ""
        self.set_all_nodes_unvisited()
        queue.empty()
        queue.add(source)
        node_string = ""
        current_node = source

        while not queue.is_empty() and current_node.data != target.data:
            current_node = queue.poll()

            if current_node.is_visited():
                continue

            current_node.set_visited(True)

            minimum_cost_node = None
            minimum_cost = sys.maxsize

            for edge in current_node.get_edges():
                new_neighbor_cost = current_node.get_cost() + edge.get_weight()
                if new_neighbor_cost < edge.get_node().get_cost():
                    edge.get_node().set_cost(new_neighbor_cost)
                if new_neighbor_cost < minimum_cost:
                    minimum_cost = new_neighbor_cost
                    minimum_cost_node = edge.get_node()
                    
            queue.add(minimum_cost_node)





    # Print adjacent nodes and weights
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
                node_string += str(current_node) + "\n\t"

                for edge in current_node.get_edges():
                    if not edge.get_node().is_visited():
                        node_string += str(edge.get_weight()) + " -> " + str(edge.get_node()) + "\n\t"

            if node_string != "":
                graph_string += node_string + "\n"

        return graph_string


class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_node(self):
        return self.node

    def __str__(self):
        return "Edge[node: %s, weight: %s]" % (self.node, self.weight)


class Node:
    def __init__(self, data):
        self.edges = set()
        self.data = data
        self.visited = False
        self.active = False
        self.cost = 0

    def set_visited(self, visited):
        self.visited = visited

    def is_visited(self):
        return self.visited

    def add_edge(self, node, weight):
        node.edges.add(Edge(self, weight))
        self.edges.add(Edge(node, weight))

    def get_edges(self):
        return self.edges

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def __str__(self):
        return "[%s]" % self.data