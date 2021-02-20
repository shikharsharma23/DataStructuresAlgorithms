from LinkedList import *;

ll = LinkedList();
n1 = Node(2);
n2 = Node(3);
n3 = Node(4);
ll.head = n1;
ll.head.next = n2;
n2.next = n3;

print('Manual Build/Traversal of Linked List')
print(ll.head.data)
print(ll.head.next.data)
print(ll.head.next.next.data)

print('Traversal of Linked List')
ll.traversal()


ll.insertion_at_beginning(5)
ll.insertion_at_end(10)

print('Traversal after insertion at beginning and end')
ll.traversal()

ll.remove_item(3)

ll.remove_item(5)


print('Traversal after deletion')
ll.traversal()
