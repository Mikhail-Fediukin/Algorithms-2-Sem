from test import time_memory
import threading

clock = 0


def explore(graph, curr_key):
    global clock
    graph[curr_key]["visited"] = True
    graph[curr_key]["pre"] = clock
    clock += 1
    for key in graph[curr_key]["kids"]:
        if not graph[key]["visited"]:
            explore(graph, key)
    graph[curr_key]["post"] = clock
    clock += 1


def main():
    with open('input.txt', 'r') as infile:
        n, m = map(int, infile.readline().split())
        graph = {}
        for i in range(1, n+1):
            graph[i] = {"kids": set(),
                        "visited": False,
                        "pre": None,
                        "post": None}
        for _ in range(m):
            u, v = map(int, infile.readline().split())
            graph[u]["kids"].add(v)
    for key in graph.keys():
        if not graph[key]["visited"]:
            explore(graph, key)
    with open('output.txt', 'w') as outfile:
        for para in sorted(graph.items(), key=lambda para: 1/para[1]["post"]):
            print(para[0], end=" ", file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
