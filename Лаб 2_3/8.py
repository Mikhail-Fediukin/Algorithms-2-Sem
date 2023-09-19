from test import time_memory
import threading


def get_smallest(dictionary):
    key = -1
    mn = float("inf")
    for curr_key in dictionary.keys():
        if not dictionary[curr_key]["visited"] and dictionary[curr_key]["path"] < mn:
            mn = dictionary[curr_key]["path"]
            key = curr_key
    return key


def main():
    with open('input.txt', 'r') as infile:
        n, m = map(int, infile.readline().split())
        matrix = [[-1 for j in range(m)] for i in range(n)]
        graph = {}
        for i in range(n):
            graph[i] = {"kids": set(),
                        "path": float("inf"),
                        "visited": False}
        for _ in range(m):
            u, v, l = map(int, infile.readline().split())
            u, v = u-1, v-1
            matrix[u][v] = l
            graph[u]["kids"].add(v)
        s, f = map(int, infile.readline().split())
        s, f = s-1, f-1
    graph[s]["path"] = 0
    smallest = s
    while smallest != -1:
        for key in graph[smallest]["kids"]:
            graph[key]["path"] = min(graph[smallest]["path"] + matrix[smallest][key], graph[key]["path"])
        graph[smallest]["visited"] = True
        smallest = get_smallest(graph)
    with open("output.txt", "w") as outfile:
        print(graph[f]["path"] if graph[f]["path"] != float("inf") else -1, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
