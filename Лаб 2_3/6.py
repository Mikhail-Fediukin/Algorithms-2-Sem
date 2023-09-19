from test import time_memory
import threading
from collections import deque


def main():
    with open('input.txt', 'r') as infile:
        n, m = map(int, infile.readline().split())
        graph = {}
        for i in range(1, n+1):
            graph[i] = {"kids": set(),
                        "path": float("inf")}
        for _ in range(m):
            u, v = map(int, infile.readline().split())
            graph[u]["kids"].add(v)
            graph[v]["kids"].add(u)
        start, end = map(int, infile.readline().split())
    graph[start]["path"] = 0
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]["kids"]:
            if graph[v]["path"] == float("inf"):
                queue.append(v)
                graph[v]["path"] = graph[u]["path"] + 1
    with open('output.txt', 'w') as outfile:
        print(graph[end]["path"] if graph[end]["path"] != float("inf") else -1, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
