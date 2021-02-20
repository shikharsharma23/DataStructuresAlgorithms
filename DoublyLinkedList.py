class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.head = None


    def get(self, index: int) -> int:

        current_node = self.head;
        if current_node is None:
            return -1

        ctr = 0
        while(current_node and ctr<index):
            ctr = ctr + 1
            current_node = current_node.next
            if current_node is None:
                return -1

        return current_node.data

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val);
        new_node.next = self.head
        new_node.prev = None;
        self.head = new_node;


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node):
            if(current_node.next is None):
                current_node.next = new_node
                new_node.prev = current_node
                break

            current_node = current_node.next




    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        current_node = self.head;
        prev_node = current_node
        new_node = Node(val)

        if index == self.get_length():
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return

        ctr = 0
        while(current_node and ctr<index):
            ctr = ctr + 1
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                return

        if prev_node is None:
            return


        prev_node.next = new_node
        new_node.next = current_node
        current_node.prev = new_node
        new_node.prev = prev_node



    def print_ll(self):

        current_node = self.head
        if current_node is None:
            return

        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            if current_node is None:
                return

    def get_length(self):
        length = 0
        current_data = self.head
        while(current_data):
            current_data = current_data.next
            length = length + 1
        return length

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """



        current_node = self.head;
        prev_node = current_node

        if index==0:
            self.head = current_node.next
            current_node = None
            return

        ctr = 0
        while(current_node and ctr<index):
            ctr = ctr + 1
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                return


        prev_node.next = current_node.next;
        if current_node.next is None:
            return
        current_node.next.prev = prev_node
        current_node = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)