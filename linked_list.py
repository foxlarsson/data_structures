class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        node = Node(data)
        if self.first is None:
            self.first = node
            self.last = node
            return

        self.last.next = node
        self.last = node
        # 1 > 2 > 3 > 4

        # node.next = self.first
        # self.first = node
        # 4 > 3 > 2 > 1

    def remove(self, data):
        if self.first is None:
            return

        if self.first.data == data:
            if self.first == self.last:
                self.first = None
                self.last = None
                return
            self.first = self.first.next
            return

        node = self.first
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                if node.next is None:
                    self.last = node
                return

            node = node.next

    def insert(self, data, eval):
        if self.first is None:
            return

        node = self.first
        while node is not None:
            if node.data == eval:
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
                if new_node.next is None:
                    self.last = new_node
                return
                #  a > H > b > c
            node = node.next

    def insert_before(self, data, eval):
        if self.first is None:
            return

        if eval == self.first.data:
            new_node = Node(data)
            new_node.next = self.first

            self.first = new_node
            return

        node = self.first
        while node.next is not None:
            if node.next.data == eval:
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next

    def print(self):
        node = self.first
        while node is not None:
            print(node.data)
            node = node.next
