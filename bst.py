class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

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
            elif data <= current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    