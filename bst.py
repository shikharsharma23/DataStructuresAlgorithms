class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def delete(self, key):
        """ delete the node with the given key and return the
        root node of the tree """

        if self.data == key:
            # found the node we need to delete
            print('found')
            print(self.data)
            if self.right and self.left:

                # get the successor node and its parent
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                # "easier" case
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.data > key:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

    def _findMin(self, parent):
        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the
        # call can return both the parent to the successor and the successor

        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]

class BinarySearchTree:

    def __init__(self):
        self.root = None # we can also initialize node here as binary tree is just represetned by root node
        # Similar for linked list

    def insert_element(self, data):

        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root

        while 1:
            if data <= current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                current_node = current_node.left;
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                current_node = current_node.right

    def print_tree_in_order(self):
        self.in_order(self.root)

    def print_tree_pre_order(self):
        self.pre_order(self.root)

    def print_tree_post_order(self):
        self.post_order(self.root)

    def in_order(self, current_node):

        if current_node:
            self.in_order(current_node.left)
            print(current_node.data)
            self.in_order(current_node.right)

    def pre_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left)
            self.pre_order(current_node.right)

    def post_order(self, current_node):
        if current_node:
            self.post_order(current_node.left)
            self.post_order(current_node.right)
            print(current_node.data)

    def search_element(self, data):
        current_node = self.root
        while(current_node):
            if data==current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, data):
        if self.root:
            self.root = self.root.delete(data)

    def successor(self, node):
        if node.left.left == None:
            return [node.left, node]
        else:
            self.successor(node.left)

    def get_in_order_successor(self, node):

        return self.successor(node.right)


    def delete_iterative(self, data):

        ### TODO : HAndle corner cases
        ### TODO : add comments

        current_node = self.root
        node_to_delete = None
        parent_node_to_delete = None
        is_right_child = False
        while current_node:


            if current_node.left.data == data:
                parent_node_to_delete = current_node
                node_to_delete = current_node.left
                break
            elif current_node.right.data == data:
                parent_node_to_delete = current_node
                node_to_delete = current_node.right
                is_right_child = True
                break

            if current_node.data < data:
                    current_node = current_node.right
                    continue

            elif current_node.data > data:
                    current_node = current_node.left
                    continue

        if not node_to_delete:
            return

        else:

            if node_to_delete.left == None and node_to_delete.right == None:
                if(is_right_child):
                    parent_node_to_delete.right = None
                else:
                    parent_node_to_delete.left = None

            elif node_to_delete.left == None and node_to_delete.right != None:
                node_to_delete.data = node_to_delete.right.data
                node_to_delete.right = None

            elif node_to_delete.left != None and node_to_delete.right == None:
                node_to_delete.data = node_to_delete.left.data
                node_to_delete.left = None

            else:

               in_order_succesor, parent_in_order_succesor = self.get_in_order_successor(node_to_delete)

               if(is_right_child):
                   parent_node_to_delete.right.data = in_order_succesor.data
               else:
                   parent_node_to_delete.left.data = in_order_succesor.data


               parent_in_order_succesor.left = None

    def delete_r(self, root, data):
        ## TODO : handle remaining 3 cases
        node_to_delete_right = None
        node_to_delete_left = None

        if not root:
            return
        if root.data < data:
            node_to_delete_right = self.delete_r(root.right, data)
        elif root.data > data:
            node_to_delete_left = self.delete_r(root.left, data)
        else:
            if root.left == None and root.right == None:
                return root


        if(node_to_delete_left):
            root.left = None

        if(node_to_delete_right):
            root.right = None


    def delete_recursive(self, data):
        self.delete_r(self.root, data)














