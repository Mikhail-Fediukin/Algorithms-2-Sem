from tree_struct import Node, Tree
from test import time_memory
import threading


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        nodes = []
        for i in range(n):
            key, left, right = map(int, f.readline().split())
            if left == -1:
                left = None
            if right == -1:
                right = None
            nodes.append(Node(key, left, right))
    with open('output.txt', 'w') as f:
        tree = Tree(nodes=nodes)
        tree.construct_tree_from_indexes(index_of_root=0)
        print("CORRECT" if tree.is_correct_bst(tree.root) else "INCORRECT", file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
