from tree_struct import Node, Tree
from test import time_memory
import sys
import threading


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        nodes = []
        for i in range(n):
            key, left, right = map(int, file.readline().split())
            if left == -1:
                left = None
            if right == -1:
                right = None
            nodes.append(Node(key, left, right))
        tree = Tree(nodes=nodes)
        tree.construct_tree_from_indexes(index_of_root=0)
        tree.in_order_traversal(tree.root)
        print()
        tree.pre_order_traversal(tree.root)
        print()
        tree.post_order_traversal(tree.root)
        print()


if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    threading.stack_size(10**8)
    thread = threading.Thread(target=time_memory(main))
    thread.start()

