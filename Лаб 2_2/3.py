from tree_struct import BST
from test import time_memory
import threading


def main():
        bst = BST()
        with open('input.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()
        with open('output.txt', 'w', encoding='utf-8') as f:
            for command in text:
                ind, num = command.split()
                num = int(num)
                if ind == "+":
                    bst.insert(num)
                elif ind == ">":
                    found = bst.next(num)
                    print(found.key if found is not None else 0, file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
