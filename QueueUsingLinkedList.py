class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class QueueLL:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front: # Queue is not empty
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self):

        if not self.front:
            return

        self.front = self.front.next

        if self.front == None:
            self.rear = None

    