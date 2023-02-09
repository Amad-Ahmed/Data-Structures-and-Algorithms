class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = Node("head")
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
