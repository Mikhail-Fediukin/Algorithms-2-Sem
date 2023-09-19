from tree_struct_AVL import AVL
from test import time_memory
import threading


def main():
    avl = AVL()
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
    with open('output.txt', 'w', encoding='utf-8') as f:
        for command in text:
            ind, num = command.split()
            num = int(num)
            if ind == "insert":
                avl.insert(num)
            elif ind == "delete":
                avl.delete(num)
            elif ind == "exists":
                print("true" if avl.exists(num) else "false", file=f)
            elif ind == "prev":
                found = avl.prev(num)
                print(found.key if found is not None else "none", file=f)
            elif ind == "next":
                found = avl.next(num)
                print(found.key if found is not None else "none", file=f)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
