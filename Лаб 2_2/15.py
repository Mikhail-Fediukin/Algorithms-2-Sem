from tree_struct_AVL import Node, AVL
from test import time_memory
import threading


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
        to_delete = int(f.readline())
    tree = AVL(nodes=nodes)
    tree.construct_tree_from_indexes()
    tree.delete(to_delete)
    dictionary = tree.prepare()
    with open('output.txt', 'w', encoding='utf-8') as f:
        print(len(tree.nodes), file=f)
        for i, node in enumerate(tree.levels):
            left = node.left.key if node.left is not None else None
            right = node.right.key if node.right is not None else None
            left_i = dictionary[left] if left is not None else 0
            right_i = dictionary[right] if right is not None else 0
            print(node.key, left_i, right_i, file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()