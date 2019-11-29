"""Priority queue with a min heap implementation"""


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def poll(self):
        self.swap(0, len(self.heap) - 1)
        removed_item = self.heap.pop()
        self.heapify_down(0)
        return removed_item

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return index * 2 + 1

    def get_right_child_index(self, index):
        return index * 2 + 2

    def try_get(self, index):
        if index < 0 or index > len(self.heap) - 1:
            return None

        return self.heap[index]

    def heapify_up(self, index):
        child = self.try_get(index)
        parent_index = self.get_parent_index(index)
        parent = self.try_get(parent_index)

        if parent and parent > child:
            self.swap(parent_index, index)
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)
        left_child = self.try_get(left_child_index)
        right_child = self.try_get(right_child_index)
        parent = self.try_get(index)

        if not left_child and not right_child or not parent:
            return
        elif left_child and not right_child:
            if parent > left_child:
                self.swap(index, left_child_index)
                self.heapify_down(left_child_index)
            else:
                return
        elif left_child < right_child and parent > left_child:
            self.swap(index, left_child_index)
            self.heapify_down(left_child_index)
        elif right_child < left_child and parent > right_child:
            self.swap(index, right_child_index)
            self.heapify_down(right_child_index)

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)