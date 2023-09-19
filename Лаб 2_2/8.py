from test import time_memory
import threading


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = None


class Tree:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = nodes
        self.height_of_tree = 0

    def construct_tree_from_indexes(self, index_of_root=0):
        for index, node in enumerate(self.nodes):
            if index == index_of_root:
                node.height = 1
                self.root = node
            if node.left is not None:
                self.nodes[node.left].parent = node
                node.left = self.nodes[node.left]
            if node.right is not None:
                self.nodes[node.right].parent = node
                node.right = self.nodes[node.right]

    def mx_height(self):
        mx = 0
        for node in self.nodes:
            if node.parent is None:
                node.height = 1
                if node.height > mx:
                    mx = node.height
            else:
                if node.parent.height is not None:
                    node.height = node.parent.height + 1
                    if node.height > mx:
                        mx = node.height
                else:
                    path = [node]
                    while node.parent.height is None:
                        node = node.parent
                        path.append(node)
                    for node in path:
                        node.height = node.parent.height
                        if node.height > mx:
                            mx = node.height
        return mx


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        n = int(f.readline())
        nodes = []
        for i in range(n):
            key, left, right = map(int, f.readline().split())
            left -= 1
            right -= 1
            if left == -1:
                left = None
            if right == -1:
                right = None
            nodes.append(Node(key, left, right))
    tree = Tree(nodes=nodes)
    tree.construct_tree_from_indexes(index_of_root=0)
    with open('output.txt', 'w', encoding='utf-8') as f:
        print(tree.mx_height(), file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
