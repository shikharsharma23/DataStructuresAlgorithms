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