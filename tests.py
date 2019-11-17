from stack import *
from queue import *

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


if __name__ == "__main__":
    stack = Stack()
    stack_test_push(stack)
    stack_test_pop(stack)
    queue = Queue()
    queue_test_add(queue)
    queue_test_poll(queue)
    print("All tests passed")