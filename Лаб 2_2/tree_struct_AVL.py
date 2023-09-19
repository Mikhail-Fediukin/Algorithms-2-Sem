from collections import deque


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1
        self.size = 1


class AVL:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = nodes if nodes is not None else []
        self.levels = []

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
        self.level_traversal(self.root)
        self.get_heights_and_sizes()

    def level_traversal(self, root):
        self.levels = []
        if root is None:
            return None
        q = deque()
        q.append(root)
        while not len(q) == 0:
            node = q.popleft()
            self.levels.append(node)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def get_heights_and_sizes(self):
        for node in self.levels[::-1]:
            if node.left is None and node.right is None:
                node.height = 1
                node.size = 1
            else:
                right_h = node.right.height if node.right is not None else 0
                left_h = node.left.height if node.left is not None else 0
                right_s = node.right.size if node.right is not None else 0
                left_s = node.left.size if node.left is not None else 0
                node.height = 1 + max(right_h, left_h)
                node.size = 1 + right_s + left_s

    def small_left_rot(self, root):
        a = root
        b = root.right
        n = a.left.height if a.left is not None else 0
        m = b.left.height if b.left is not None else 0
        k = b.right.height if b.right is not None else 0
        a.height = max(n, m) + 1
        b.height = max(a.height, k) + 1

        n_s = a.left.size if a.left is not None else 0
        m_s = b.left.size if b.left is not None else 0
        k_s = b.right.size if b.right is not None else 0
        a.size = n_s + m_s + 1
        b.size = a.size + k_s + 1

        y = b.left
        b.left = a
        if y is not None:
            y.parent = a
        a.right = y
        b.parent = a.parent
        if a.parent is not None:
            if a.parent.right == a:
                a.parent.right = b
            else:
                a.parent.left = b
        a.parent = b
        if root == self.root:
            self.root = b
        while b.parent is not None:
            b = b.parent
            b.height -= 1

    def small_right_rot(self, root):
        a = root
        b = root.left

        n = a.right.height if a.right is not None else 0
        m = b.right.height if b.right is not None else 0
        k = b.left.height if b.left is not None else 0
        a.height = max(n, m) + 1
        b.height = max(a.height, k) + 1

        n_s = a.right.size if a.right is not None else 0
        m_s = b.right.size if b.right is not None else 0
        k_s = b.left.size if b.left is not None else 0
        a.size = n_s + m_s + 1
        b.size = a.size + k_s + 1

        y = b.right
        b.right = a
        if y is not None:
            y.parent = a
        a.left = y
        b.parent = a.parent
        if a.parent is not None:
            if a.parent.left == a:
                a.parent.left = b
            else:
                a.parent.right = b
        a.parent = b
        if root == self.root:
            self.root = b
        while b.parent is not None:
            b = b.parent
            b.height -= 1

    def big_left_rot(self, root):
        a = root
        b = a.right
        c = b.left

        m = a.left.height if a.left is not None else 0
        n = c.left.height if c.left is not None else 0
        k = c.right.height if c.right is not None else 0
        p = b.right.height if b.right is not None else 0
        a.height = max(m, n) + 1
        b.height = max(k, p) + 1
        c.height = max(a.height, b.height) + 1

        m_s = a.left.size if a.left is not None else 0
        n_s = c.left.size if c.left is not None else 0
        k_s = c.right.size if c.right is not None else 0
        p_s = b.right.size if b.right is not None else 0
        a.size = m_s + n_s + 1
        b.size = k_s + p_s + 1
        c.size = a.size + b.size + 1

        x = c.left
        y = c.right
        c.parent = None
        b.left = y
        if y is not None:
            y.parent = b
        c.right = b
        b.parent = c
        c.left = a
        c.parent = a.parent
        if a.parent is not None:
            if a.parent.right == a:
                a.parent.right = c
            else:
                a.parent.left = c
        a.parent = c
        a.right = x
        if x is not None:
            x.parent = a
        if root == self.root:
            self.root = c
        while c.parent is not None:
            c = c.parent
            c.height -= 1

    def big_right_rot(self, root):
        a = root
        b = a.left
        c = b.right

        m = a.right.height if a.right is not None else 0
        n = c.right.height if c.right is not None else 0
        k = c.left.height if c.left is not None else 0
        p = b.left.height if b.left is not None else 0
        a.height = max(m, n) + 1
        b.height = max(k, p) + 1
        c.height = max(a.height, b.height) + 1

        m_s = a.right.size if a.right is not None else 0
        n_s = c.right.size if c.right is not None else 0
        k_s = c.left.size if c.left is not None else 0
        p_s = b.left.size if b.left is not None else 0
        a.size = m_s + n_s + 1
        b.size = k_s + p_s + 1
        c.size = a.size + b.size + 1

        x = c.right
        y = c.left
        c.parent = None
        b.right = y
        if y is not None:
            y.parent = b
        c.left = b
        b.parent = c
        c.right = a
        c.parent = a.parent
        if a.parent is not None:
            if a.parent.left == a:
                a.parent.left = c
            else:
                a.parent.right = c
        a.parent = c
        a.left = x
        if x is not None:
            x.parent = a
        if root == self.root:
            self.root = c
        while c.parent is not None:
            c = c.parent
            c.height -= 1

    @staticmethod
    def get_balance(node):
        right = node.right.height if node.right is not None else 0
        left = node.left.height if node.left is not None else 0
        return right - left

    def rebalance(self, node):
        balance = self.get_balance(node)
        if abs(balance) <= 1:
            return
        if balance > 0:  # left rot
            if self.get_balance(node.right) < 0:
                self.big_left_rot(node)
            else:
                self.small_left_rot(node)
        else:  # right rot
            if self.get_balance(node.left) > 0:
                self.big_right_rot(node)
            else:
                self.small_right_rot(node)

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

    def insert(self, k):
        node = Node(k)
        self.nodes.append(node)
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
                node = node.parent if node.parent is not None else None
                while node is not None:
                    right_h = node.right.height if node.right is not None else 0
                    left_h = node.left.height if node.left is not None else 0
                    right_s = node.right.size if node.right is not None else 0
                    left_s = node.left.size if node.left is not None else 0
                    node.height = max(right_h, left_h) + 1
                    node.size = right_s + left_s + 1
                    next = node.parent
                    self.rebalance(node)
                    node = next

    def prepare(self):
        self.level_traversal(self.root)
        d = {self.levels[i].key: i+1 for i in range(len(self.levels))}
        return d

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

    def delete(self, k):
        if self.root is None:
            return
        found_node, status = self.find(k, self.root)
        if status == "ok":

            if found_node == self.root and len(self.nodes) == 1:
                self.root = None
                self.nodes = []
                return

            if found_node.right is None and found_node.left is None:
                node = found_node.parent
                if node.left == found_node:
                    node.left = None
                else:
                    node.right = None

            elif found_node.left is None:
                node = found_node.parent
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
                to_be_back = node_to_insert.parent
                if node_to_insert != found_node.left:
                    node = to_be_back
                else:
                    node = node_to_insert

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

            while node is not None:
                right_h = node.right.height if node.right is not None else 0
                left_h = node.left.height if node.left is not None else 0
                right_s = node.right.size if node.right is not None else 0
                left_s = node.left.size if node.left is not None else 0
                node.height = max(right_h, left_h) + 1
                node.size = right_s + left_s + 1
                next = node.parent
                self.rebalance(node)
                node = next

            self.nodes.remove(found_node)

    def next(self, node):
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

    @staticmethod
    def get_k_elem(k, root):
        if root is None or k > root.size or k < 0:
            return
        while True:
            if root is None:
                return
            left_s = root.left.size if root.left is not None else 0
            if k == left_s + 1:
                return root
            elif k < left_s + 1:
                root = root.left
            elif k > left_s + 1:
                k -= (left_s + 1)
                root = root.right

