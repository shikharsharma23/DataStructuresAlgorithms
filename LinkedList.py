class Node:
    def __init__(self, data):
        self.data = data # for hashmap, data can be a key value tuple
        self.next = None

class LinkedList:
    def __init__(self): # In this case, user needs to manually attach a head node to Linked List object.
        # an alternate is to take the first node while
        # declaring the linked list and mantain it as head node
        self.head = None

    def traversal(self): # a pointer will start from head and iterate over the list
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next;

    def insertion_at_end(self, data):
        current_node = self.head
        while current_node:
            if current_node.next is None:
                current_node.next = Node(data);
                break
            current_node = current_node.next

    def insertion_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_item(self, data):

        current_node = self.head

        if current_node is None:
            return

        if current_node.data == data:
            self.head = current_node.next;
            return

        while current_node:
            previous_node = current_node;
            current_node = current_node.next
            if current_node is None:
                return
            if current_node.data == data:
                previous_node.next = current_node.next;
                current_node = None









