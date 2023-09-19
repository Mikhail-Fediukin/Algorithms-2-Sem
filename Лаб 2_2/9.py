from test import time_memory
import threading


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1


class Tree:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = nodes

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
        self.get_sizes()

    def get_sizes(self):
        for node in self.nodes:
            while node.parent is not None:
                node.parent.size += 1
                node = node.parent

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

    def delete_altogether(self, key):
        found = self.find(key, root=self.root)
        if found[1] == "ok" and found[0] is not None:
            node = found[0]
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            curr_node = node
            while curr_node.parent is not None:
                curr_node.parent.size -= node.size
                curr_node = curr_node.parent
            node.parent = None
        return self.root.size


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        nodes = []
        for i in range(n):
            key, left, right = map(int, file.readline().split())
            left, right = left-1, right-1
            if left == -1:
                left = None
            if right == -1:
                right = None
            nodes.append(Node(key, left, right))
        tree = Tree(nodes=nodes)
        tree.construct_tree_from_indexes(index_of_root=0)
        m = int(file.readline())
        to_del = map(int, file.readline().split())
    with open('output.txt', 'w') as file:
        for key in to_del:
            print(tree.delete_altogether(key), file=file)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
