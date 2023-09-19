from tree_struct_AVL import AVL
from test import time_memory
import threading


def main():
    tree = AVL()
    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as out_file:
            n = int(file.readline())
            for _ in range(n):
                command, number = file.readline().split()
                if command == '+1' or command == '1':
                    tree.insert(int(number))
                elif command == '-1':
                    tree.delete(int(number))
                elif command == '0':
                    number = int(number)
                    print(tree.get_k_elem(len(tree.nodes) - number + 1, tree.root).key, file=out_file)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
