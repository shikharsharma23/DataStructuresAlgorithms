class MinHeap:

    def __init__(self, maxsize):
        self.heap = [None]*maxsize
        self.root = 0
        self.size = 0
        self.maxsize = maxsize



    def parent(self, pos):
        return (pos - 1)//2


    def leftChild(self, pos):
        '''return position of left chold'''
        return 2*pos + 1


    def rightChild(self, pos):
        '''return position of right child'''
        return 2*pos + 2


    def isLeaf(self, pos):
        if pos >= ((self.size-1)//2) and pos <= self.size:
            return True
        return False


    def swap(self, fpos, spos):
        '''Swpa two node values in heap'''
        self.heap[fpos],self.heap[spos] = self.heap[spos], self.heap[fpos]


    def minHeapify(self, pos):
        '''Make sure everything below this position is heapified'''
        if not self.isLeaf(pos):
            if self.heap[pos] > self.heap[self.leftChild(pos)] or self.heap[pos] > self.heap[self.rightChild(pos)]:
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]: # swap with the left child and heapify the left child
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))


    def insert(self, element):
        '''inserts an element to heap'''
        if self.size == 0:
            self.heap[self.root] = element
            self.size = self.size + 1
            return
        else:
            if self.maxsize == self.size:
                return
            else:

                self.heap[self.size] = element
                current = self.size
                self.size = self.size + 1

                while self.heap[current] < self.heap[self.parent(current)] :

                    self.swap(current, self.parent(current))
                    current = self.parent(current)
                    if current == 0:
                        break

    def print(self):
        '''prints the heap'''
        for i in range(0, self.size):
            print(self.heap[i], end = ',')


    def buildMinHeap(self, data):
        '''Accept an array of data and return the heap form'''
        self.heap[0:len(data)] = data
        self.size = len(data)
        for i in range(self.size//2, 0, -1):
            self.minHeapify(i)
        return self.heap


    def remove(self):
        ele_to_delete = self.heap[self.root]
        self.heap[self.root] = self.heap[self.size-1]
        self.size = self.size - 1
        self.minHeapify(0)
        return ele_to_delete
