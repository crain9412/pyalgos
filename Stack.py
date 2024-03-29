"""Stack with a singly linked list implementation for O(1) push and pop"""


class Stack:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        current = self.head
        list_string = ""
        
        while current is not None:
            if current.get_next() is not None:
                list_string += str(current) + " -> "
            else:
                list_string += str(current)

            current = current.get_next()

        return list_string
    
    def push(self, data):
        created_node = Node(data)
        old_head = self.head

        if old_head is not None:
            created_node.set_next(old_head)

        self.head = created_node

    def pop(self):
        removed_node = self.head

        if self.head is None:
            return None
        else:
            self.head = self.head.get_next()

        return removed_node.get_data()

    def is_empty(self):
        return not self.head

    def empty(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "[%s]" % str(self.data)

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data
