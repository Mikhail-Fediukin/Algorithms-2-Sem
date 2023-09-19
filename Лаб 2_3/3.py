from test import time_memory
import threading


def explore(graph, visited, curr_key):
    visited[curr_key] = True
    for key in graph[curr_key]:
        if visited[key]:
            return False
        return explore(graph, visited, key)
    return True


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
    flag = False
    for key in graph.keys():
        for i in range(1, n + 1):
            visited[i] = False
        outcome = explore(graph, visited, key)
        if not outcome:
            flag = True
            break
    with open('output.txt', 'w') as outfile:
        print(1 if flag else 0, file=outfile)


if __name__ == '__main__':
    thread = threading.Thread(target=time_memory(main))
    thread.start()
