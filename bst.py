"""Balanced Binary Search Tree that can insert, find and delete elements."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class BalancedTree:
    def __init__(self):
        self.root_node: Node = None

    def insert(self, data) -> None:
        """Insert a data into tree"""
        self.root_node = self.insert_to_node(self.root_node, data)

    def insert_to_node(self, node, data) -> Node:
        """Insert a data into selected node"""
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insert_to_node(node.left, data)
        else:
            node.right = self.insert_to_node(node.right, data)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def find(self, data):
        """Find a data in tree"""
        return self.find_in_node(self.root_node, data)

    def find_in_node(self, node, data):
        """Find a data in selected node"""
        if not node:
            return False
        if node.data == data:
            return node

        if node.data < data:
            return self.find_in_node(node.right, data)

        return self.find_in_node(node.left, data)

    def delete(self, data):
        """Delete a data from tree"""
        self.root_node = self.delete_from_node(self.root_node, data)

    def delete_from_node(self, node, data):
        """Delete a data from selected node"""
        if not node:
            return None

        if data < node.data:
            node.left = self.delete_from_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_from_node(node.right, data)
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
                if not temp:
                    temp = node
                    node = None
                else:
                    node = temp
                del temp
            else:
                temp = self.min_value_node(node.right)
                node.data = temp.data
                node.right = self.delete_from_node(node.right, temp.data)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left),
                              self. get_height(node.right))

        balance = self. get_balance(node)

        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        """Find node with lowest value"""
        current = node

        while current.left is not None:
            current = current.left

        return current

    def get_height(self, node):
        """Obtain height from node"""
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        """Obtain total balance count for node"""
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        """Rotate the tree to the right"""
        left_node = node.left
        if left_node is None:
            return node
        right_node = left_node.right

        left_node.right = node
        node.left = right_node

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right))
        left_node.height = (
            1 + max(
                self.get_height(left_node.left),
                self.get_height(left_node.right)
            )
        )

        return left_node

    def left_rotate(self, node):
        """Rotate the tree to the left"""
        right_node = node.right
        if right_node is None:
            return node
        left_node = right_node.left

        right_node.left = node
        node.right = left_node

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right))
        right_node.height = (
            1 + max(
                self.get_height(right_node.left),
                self.get_height(right_node.right)
            )
        )

        return right_node
