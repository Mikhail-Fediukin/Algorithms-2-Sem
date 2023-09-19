from test import time_memory
import threading


def explore(graph, visited, curr_key):
    visited[curr_key] = True
    for q in graph[curr_key]:
        if not visited[q]:
            explore(graph, visited, q)


def main():
    with open('input.txt', 'r') as infile:
        n, m = map(int, infile.readline().split())
        graph = {}
        visited = {}
        for i in range(1, n+1):
            graph[i] = set()
            visited[i] = False
        for _ in range(m):
            u, v = map(int, infile.readline().split())
            graph[u].add(v)
            graph[v].add(u)
    counter = 0
    for q in graph.keys():
        if not visited[q]:
            counter += 1
            explore(graph, visited, q)
    with open('output.txt', 'w') as outfile:
        print(counter, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
