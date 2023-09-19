from collections import deque
from test import time_memory
import threading


def cycle(graph, start_key):
    queue = deque()
    queue.append(start_key)
    while len(queue) > 0:
        curr_key = queue.pop()
        graph[curr_key]["visited"] = True
        for key in graph[curr_key]["kids"]:
            if key == start_key:
                return True
            if not graph[key]["visited"]:
                queue.append(key)
    return False


def main():
    n = int(input())
    graph = {}
    for _ in range(n):
        key = input()
        graph[key] = {"kids": set(),
                      "visited": False}
        m = int(input())
        for _ in range(m):
            kid = input()
            graph[key]["kids"].add(kid)
        input()
    for start_key in graph.keys():
        flag = True
        for key in graph.keys():
            graph[key]["visited"] = False
        print("YES" if cycle(graph, start_key) else "NO")


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()