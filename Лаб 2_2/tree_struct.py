import sys
from collections import deque

sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class Tree:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = nodes

    def check(self, v, mn, mx):
        if v is None:
            return True
        if v.key <= mn or mx <= v.key:
            return False
        return self.check(v.left, mn, v.key) and self.check(v.right, v.key, mx)

    def check_eq(self, v, mn, mx):
        if v is None:
            return True
        if v.key < mn or mx <= v.key:
            return False
        return self.check_eq(v.left, mn, v.key) and self.check_eq(v.right, v.key, mx)

    def is_correct_bst(self, root, with_equal=False):
        if with_equal:
            return self.check_eq(root, float("-inf"), float("+inf"))
        return self.check(root, float("-inf"), float("+inf"))

    def construct_tree_from_keys(self, key_of_root=None):
        for node_to_change in self.nodes:
            for node in self.nodes:
                if key_of_root is not None and node.key == key_of_root:
                    self.root = node
                if node_to_change.left == node.key:
                    node.parent = node_to_change
                    node_to_change.left = node
                if node_to_change.right == node.key:
                    node.parent = node_to_change
                    node_to_change.right = node
        if key_of_root is None:
            for node in self.nodes:
                if node.parent is None:
                    self.root = node

    def construct_tree_from_indexes(self, index_of_root=0):
        for index, node in enumerate(self.nodes):
            if index == index_of_root:
                self.root = node
            if node.left is not None:
                self.nodes[node.left].parent = node
                node.left = self.nodes[node.left]
            if node.right is not None:
                self.nodes[node.right].parent = node
                node.right = self.nodes[node.right]

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def size(self, root):
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def in_order_traversal(self, root):
        if root is None:
            return
        self.in_order_traversal(root.left)
        print(root.key, end=" ")
        self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root is None:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.key, end=" ")

    @staticmethod
    def level_traversal(root):
        if root is None:
            return None
        q = deque()
        q.append(root)
        while not len(q) == 0:
            node = q.popleft()
            print(node.key)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


class BST:
    def __init__(self, root=None):
        self.root = root
        self.counter = 0

    def find(self, k, root=None):
        if root is None or root.key == k:
            return root, "ok"
        elif k < root.key:
            if root.left is None:
                return root, "take_left_kid"
            return self.find(k, root.left)
        else:
            if root.right is None:
                return root, "take_right_kid"
            return self.find(k, root.right)

    def exists(self, k, root=None):
        if root is None:
            root = self.root
        found, status = self.find(k, root)
        return True if status == "ok" else False

    def find_by_key(self, k, root=None, file=None):
        if root is None:
            root = self.root
            self.counter = 0
        if root.left is not None:
            self.find_by_key(k, root.left, file)
        else:
            self.counter += 1
        if k == self.counter:
            if file is not None:
                with open(file, 'a', encoding='utf-8') as file:
                    print(root.key, file=file)
            else:
                print(root.key)
        if root.right is not None:
            self.find_by_key(k, root.right, file)
        else:
            self.counter += 1

    def insert(self, k):
        node = Node(k)
        if self.root is None:
            self.root = node
        else:
            found_node, status = self.find(k, self.root)
            if status != "ok":
                if status == "take_left_kid":
                    node.parent = found_node
                    found_node.left = node
                else:
                    node.parent = found_node
                    found_node.right = node

    def delete(self, k):
        if self.root is None:
            return
        found_node, status = self.find(k, self.root)
        if status == "ok":

            if found_node == self.root and self.root.right is None and self.root.left is None:
                self.root = None
                return

            if found_node.right is None and found_node.left is None:
                node = found_node.parent
                if node.left == found_node:
                    node.left = None
                else:
                    node.right = None

            elif found_node.left is None:
                if found_node.parent is not None:
                    if found_node.parent.left == found_node:
                        found_node.parent.left = found_node.right
                        found_node.right.parent = found_node.parent
                    else:
                        found_node.parent.right = found_node.right
                        found_node.right.parent = found_node.parent
                else:
                    found_node.right.parent = None
                    self.root = found_node.right
            else:

                node_to_insert = found_node.left
                while node_to_insert.right is not None:
                    node_to_insert = node_to_insert.right

                if node_to_insert.parent.right == node_to_insert:
                    node_to_insert.parent.right = None
                else:
                    node_to_insert.parent.left = None

                node_to_insert.parent = found_node.parent

                if found_node.parent is not None:
                    if found_node.parent.right == found_node:
                        found_node.parent.right = node_to_insert
                    else:
                        found_node.parent.left = node_to_insert

                node_to_insert.right = found_node.right
                if found_node.right is not None:
                    found_node.right.parent = node_to_insert

                if found_node.left != node_to_insert and found_node.left is not None:
                    found_node.left.parent = node_to_insert
                    y = node_to_insert.left
                    node_to_insert.left = found_node.left
                    if y is not None:
                        node_to_insert.left.right = y
                        y.parent = node_to_insert.left

                if found_node == self.root:
                    self.root = node_to_insert
                found_node.right = None

    def tree_min(self, root=None):
        if root is None:
            root = self.root
        while root.left is not None:
            root = root.left
        return root

    def tree_max(self, root=None):
        if root is None:
            root = self.root
        while root.right is not None:
            root = root.right
        return root

    def k_max(self, n):
        n -= 1
        mx = self.tree_max(self.root)
        while n != 0:
            mx = self.prev(mx)
            n -= 1
        return mx.key

    def next(self, node):
        if self.root is None:
            return
        if type(node) is int:
            k = node
            node, status = self.find(node, root=self.root)
            if status != "ok":
                artificial_node = Node(k)
                artificial_node.parent = node
                node = artificial_node
        if node.right is not None:
            return self.tree_min(node.right)
        else:
            return self.right_ancestor(node)

    def right_ancestor(self, node):
        if node.parent is None or node.key < node.parent.key:
            return node.parent
        else:
            return self.right_ancestor(node.parent)

    def prev(self, node):
        if self.root is None:
            return
        if type(node) is int:
            k = node
            node, status = self.find(node, root=self.root)
            if status != "ok":
                artificial_node = Node(k)
                artificial_node.parent = node
                node = artificial_node
        if node.left is not None:
            return self.tree_max(node.left)
        else:
            return self.left_ancestor(node)

    def left_ancestor(self, node):
        if node.parent is None or node.key >= node.parent.key:
            return node.parent
        else:
            return self.left_ancestor(node.parent)
