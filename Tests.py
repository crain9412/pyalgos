from Stack import Stack
from Queue import Queue
from Mergesort import *
from Quicksort import *
from Graph import *
from PriorityQueue import *

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

    animal = Node("Animal")
    mammal = Node("Mammal")
    cat = Node("Cat")
    dog = Node("Dog")
    tool = Node("Tool")
    hammer = Node("Hammer")
    tree = Node("Tree")
    goes = Node("Goes")
    forever = Node("Forever")

    animal.add_adjacent_node(mammal)
    mammal.add_adjacent_node(cat)
    mammal.add_adjacent_node(dog)
    tool.add_adjacent_node(hammer)
    goes.add_adjacent_node(forever)
    forever.add_adjacent_node(goes)

    graph.add_node(animal)
    graph.add_node(mammal)
    graph.add_node(cat)
    graph.add_node(dog)
    graph.add_node(tool)
    graph.add_node(hammer)
    graph.add_node(tree)
    graph.add_node(goes)
    graph.add_node(forever)

    assert(graph.breadth_first_search(animal, "Dog") is not None), "Breadth first search should find Dog from Animal"
    assert(graph.breadth_first_search(tool, "Hammer") is not None), "Depth first search should find Hammer from Tool"
    assert(graph.breadth_first_search(mammal, "Hammer") is None), "Depth first search shouldn't find Hammer from Mammal"
    assert(graph.has_cycle()), "Graph should have a cycle, has cycle should return true"
    graph.remove_node(goes)
    graph.remove_node(forever)
    assert(not graph.has_cycle()), "Graph should no longer have a cycle"


def priority_queue_test():
    priority_queue = PriorityQueue()

    priority_queue.add(1)
    priority_queue.add(8)
    priority_queue.add(5)
    priority_queue.add(3)
    priority_queue.add(4)
    priority_queue.add(2)
    priority_queue.add(6)
    priority_queue.add(7)
    priority_queue.add(0)

    i = 0

    # this effectively tests heap sort as well...
    while not priority_queue.is_empty():
        number_polled = priority_queue.poll()
        assert(number_polled == i), "Expected %s got %s from priority queue" % (i, number_polled)
        i = i + 1


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
    priority_queue_test()
    print("All tests passed")