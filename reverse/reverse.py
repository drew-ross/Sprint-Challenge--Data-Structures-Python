class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node:
            s = []
            current = node
            s.append(current)
            while current.get_next():
                s.append(current.get_next())
                current = current.get_next()
            self.head = s.pop()
            while len(s) > 1:
                current.set_next(s[-1])
                current = s.pop()
            if len(s) == 1:
                last = s.pop()
                last.set_next(None)

