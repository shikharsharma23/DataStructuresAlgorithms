class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """

        self.maxlen = k
        self.currlen = 0
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        tail = (self.tail + 1) % self.maxlen
        self.queue[tail] = value
        self.tail = tail
        self.currlen += 1
        if self.currlen == 1:
            self.head = 0

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.maxlen
        self.currlen -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.currlen == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.currlen == self.maxlen

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()