"""Queue with a doubly linked list implementation for O(1) queue and dequeue"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return "[%s]" % str(self.data)

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        list_string = ""

        while current is not None:
            if current.get_next() is not None:
                list_string += str(current) + " <-> "
            else:
                list_string += str(current)

            current = current.get_next()

        return list_string

    def add(self, data):
        created_node = Node(data)

        if self.head is None:
            self.head = created_node
            self.tail = created_node
        else:
            old_tail = self.tail
            self.tail = created_node
            self.tail.set_prev(old_tail)
            old_tail.set_next(self.tail)

    def poll(self):
        removed_node = self.head

        if removed_node is None:
            return None
        else:
            self.head = removed_node.get_next()

        return removed_node.get_data()

    def is_empty(self):
        return not self.head

    def empty(self):
        self.head = None
        self.tail = None
