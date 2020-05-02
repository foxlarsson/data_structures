class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkedList:
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
        node.prev = self.last
        self.last = node

        # a > b > c > D

    def insert(self, data, eval):
        if self.first is None:
            return

        node = self.first
        while node is not None:
            if node.data == eval:
                new_node = Node(data)
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                if new_node.next is None:
                    self.last = new_node
                else:
                    new_node.next.prev = new_node
                return
            node = node.next

    def remove(self, data):
        if self.first is None:
            return

        if self.first.data == data:
            if self.first == self.last:
                self.first = None
                self.last = None
                return
            self.first.next.prev = None
            self.first = self.first.next

        node = self.first
        while node is not None:
            if node.data == data:
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.last = node.prev
            node = node.next

    def print(self, reverse=False):
        if self.first is None:
            print(self.first)

        if reverse is True:
            node = self.last
        else:
            node = self.first

        while node is not None:
            if node.prev is None:
                print(node.prev, end=' ')
            else:
                print(node.prev.data, end=' ')

            print(node.data, end=' ')

            if node.next is None:
                print(node.next)
            else:
                print(node.next.data)

            if reverse is True:
                node = node.prev
            else:
                node = node.next
        print()
