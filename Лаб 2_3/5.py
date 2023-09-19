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
        graph_t = {}
        for i in range(1, n+1):
            graph[i] = {"kids": set(),
                        "visited": False,
                        "pre": None,
                        "post": None}
            graph_t[i] = {"kids": set(),
                        "visited": False,
                        "pre": None,
                        "post": None}
        for _ in range(m):
            u, v = map(int, infile.readline().split())
            graph[u]["kids"].add(v)
            graph_t[v]["kids"].add(u)
    for key in graph_t.keys():
        if not graph_t[key]["visited"]:
            explore(graph_t, key)
    scc = 0
    for para in sorted(graph_t.items(), key=lambda para: 1 / para[1]["post"]):
        if not graph[para[0]]["visited"]:
            scc += 1
            explore(graph, para[0])
    with open('output.txt', 'w') as outfile:
        print(scc, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
