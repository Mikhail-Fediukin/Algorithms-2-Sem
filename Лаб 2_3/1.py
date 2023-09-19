from test import time_memory
import threading

found = False


def explore(graph, visited, curr_key, goal):
    global found
    if curr_key == goal:
        found = True
        return
    visited[curr_key] = True
    for key in graph[curr_key]:
        if not visited[key]:
            explore(graph, visited, key, goal)


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
        u, v = map(int, infile.readline().split())
    explore(graph, visited, u, v)
    with open('output.txt', 'w') as outfile:
        print(1 if found else 0, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
