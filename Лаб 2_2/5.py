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
            if ind == "insert":
                bst.insert(num)
            elif ind == "delete":
                bst.delete(num)
            elif ind == "exists":
                print("true" if bst.exists(num) else "false", file=f)
            elif ind == "prev":
                found = bst.prev(num)
                print(found.key if found is not None else "none", file=f)
            elif ind == "next":
                found = bst.next(num)
                print(found.key if found is not None else "none", file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()