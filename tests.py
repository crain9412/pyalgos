from stack import Stack
from queue import Queue
from mergesort import *
from quicksort import *
from graph import *

def stack_test_push(stack):
    stack.push(1)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert(str(stack) == "[3] -> [2] -> [1] -> [1]"), "Stack should currently contain 3, 2, 1, 1"


def stack_test_pop(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    last_element = stack.pop()
    assert(last_element == 1), "Last element removed should be the first element pushed"
    assert(str(stack) == ""), "Stack should be empty"


def queue_test_add(queue):
    queue.add("A")
    queue.add("B")
    queue.add("C")
    queue.add("C")
    assert(str(queue) == "[A] <-> [B] <-> [C] <-> [C]"), "Queue should currently contain A, B, C, C"


def queue_test_poll(queue):
    queue.poll()
    queue.poll()
    queue.poll()
    last_element = queue.poll()
    assert(last_element == "C"), "Last element removed should be the last element added"
    assert(str(queue) == ""), "Queue should be empty"


def mergesort_test():
    array = [5, 3, 1, 2, 4, 5]
    array = mergesort(array)
    assert(array == [1, 2, 3, 4, 5, 5]), "Merge sort should've sorted these items"


def quicksort_test():
    array = [5, 3, 1, 2, 4, 5]
    quicksort(array)
    assert (array == [1, 2, 3, 4, 5, 5]), "Quick sort should've sorted these items"


def graph_test():
    graph = Graph()

    node_a = Node("Animal")
    node_b = Node("Mammal")
    node_c = Node("Cat")
    node_d = Node("Dog")
    node_e = Node("Hammer")
    node_f = Node("Axe")
    node_g = Node("Tree")

    node_a.add_adjacent_node(node_b)
    node_b.add_adjacent_node(node_c)
    node_b.add_adjacent_node(node_d)
    #node_d.add_adjacent_node(node_a)
    node_e.add_adjacent_node(node_f)

    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)
    graph.add_node(node_e)
    graph.add_node(node_f)
    graph.add_node(node_g)

    print(str(graph))


if __name__ == "__main__":
    stack = Stack()
    stack_test_push(stack)
    stack_test_pop(stack)
    queue = Queue()
    queue_test_add(queue)
    queue_test_poll(queue)
    mergesort_test()
    quicksort_test()
    graph_test()
    print("All tests passed")