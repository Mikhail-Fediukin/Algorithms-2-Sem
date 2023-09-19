from collections import deque


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    graph = {}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "#":
                graph[i * m + j] = {"kids": set(),
                                    "visited": False}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != "#":
                continue
            key = i * m + j
            neighbours = []
            if i-1 >= 0 and matrix[i-1][j] == "#":
                neighbours.append((i-1) * m + j)
            if i+1 < n and matrix[i+1][j] == "#":
                neighbours.append((i+1) * m + j)
            if j-1 >= 0 and matrix[i][j-1] == "#":
                neighbours.append(i * m + (j-1))
            if j+1 < m and matrix[i][j+1] == "#":
                neighbours.append(i * m + (j+1))
            for v in neighbours:
                graph[key]["kids"].add(v)
                graph[v]["kids"].add(key)
    queue = deque()
    counter = 0
    for overall_key in graph.keys():
        if not graph[overall_key]["visited"]:
            counter += 1
            queue.append(overall_key)
            while len(queue) > 0:
                curr_key = queue.pop()
                graph[curr_key]["visited"] = True
                for key in graph[curr_key]["kids"]:
                    if not graph[key]["visited"]:
                        queue.append(key)
    print(counter)
