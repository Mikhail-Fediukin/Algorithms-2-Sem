from collections import deque
from test import time_memory
import threading


def inverted(n):
    return 1 if n == 0 else 0


def main():
    with open('input.txt', 'r') as infile:
        n, m = map(int, infile.readline().split())
        graph = {}
        for i in range(1, n+1):
            graph[i] = {"kids": set(),
                        "visited": False,
                        "color": -1}
        for _ in range(m):
            u, v = map(int, infile.readline().split())
            graph[u]["kids"].add(v)
            graph[v]["kids"].add(u)
    flag = True
    graph[1]["color"] = 0
    queue = deque()
    queue.append(1)
    while len(queue) > 0:
        u = queue.popleft()
        graph[u]["visited"] = True
        for v in graph[u]["kids"]:
            if not graph[v]["visited"]:
                graph[v]["color"] = inverted(graph[u]["color"])
                queue.append(v)
            else:
                if graph[v]["color"] != inverted(graph[u]["color"]):
                    flag = False
                    break
    with open('output.txt', 'w') as outfile:
        print(1 if flag else 0, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
