class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        if self.front == None:
            self.front = Node(data)
            self.rear = self.front
            self.rear.next = self.front
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            self.front = self.front.next
            self.size -= 1

    def printQueue(self):
        itr = self.front
        while itr:
            print(itr.data)
            itr = itr.next
