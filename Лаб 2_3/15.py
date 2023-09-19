from collections import deque


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    graph = {}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "0":
                graph[i * m + j] = {"kids": set(),
                                    "path": float("inf")}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != "0":
                continue
            key = i * m + j
            neighbours = []
            if i-1 >= 0 and matrix[i-1][j] == "0":
                neighbours.append((i-1) * m + j)
            if i+1 < n and matrix[i+1][j] == "0":
                neighbours.append((i+1) * m + j)
            if j-1 >= 0 and matrix[i][j-1] == "0":
                neighbours.append(i * m + (j-1))
            if j+1 < m and matrix[i][j+1] == "0":
                neighbours.append(i * m + (j+1))
            for v in neighbours:
                graph[key]["kids"].add(v)
                graph[v]["kids"].add(key)
    q_s, q_e, time = map(int, input().split())
    start_key = (q_s-1)*m + q_e-1
    boys = []
    for _ in range(4):
        s, e, k = map(int, input().split())
        key = (s-1)*m + e-1
        boys.append((key, k))
    graph[start_key]["path"] = 0
    queue = deque()
    queue.append(start_key)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]["kids"]:
            if graph[v]["path"] == float("inf"):
                queue.append(v)
                graph[v]["path"] = graph[u]["path"] + 1
    count = 0
    for boy in boys:
        if graph[boy[0]]["path"] <= time:
            count += boy[1]
    print(count)
