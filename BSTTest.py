from bst import *

bst = BinarySearchTree()

print('Building Tree')
bst.insert_element(6)
bst.insert_element(4)
bst.insert_element(1)
bst.insert_element(5)
bst.insert_element(10)
bst.insert_element(8)
bst.insert_element(50)
bst.insert_element(3)
bst.insert_element(33)

print('In order')
bst.print_tree_in_order()

print('Pre order')
bst.print_tree_pre_order()

print('Post order')
bst.print_tree_post_order()

print('Searching for elements')
print(bst.search_element(8))
print(bst.search_element(180))
print(bst.search_element(33))

#print('Deleting a leaf')
#bst.delete(3)

#print('In order traversal after deletion')
#bst.print_tree_in_order()

#print('Iterative Delete')
#bst.delete_iterative(5)
#bst.print_tree_in_order()

print('Self delete recursive')
bst.delete_recursive(10)
bst.print_tree_in_order()