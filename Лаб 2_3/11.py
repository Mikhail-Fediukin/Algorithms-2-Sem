from collections import deque


if __name__ == "__main__":
    n = int(input())
    graph = {}
    for _ in range(n):
        one, symbol, two = input().split()
        try:
            graph[one]["kids"].append(two)
        except KeyError:
            graph[one] = {"kids": [two],
                          "path": float("inf")}
    start = input()
    end = input()
    try:
        graph[start]["path"] = 0
    except KeyError:
        graph[start] = {"kids": [],
                        "path": 0}
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]["kids"]:
            try:
                if graph[v]["path"] == float("inf"):
                    queue.append(v)
                    graph[v]["path"] = graph[u]["path"] + 1
            except KeyError:
                graph[v] = {"kids": [],
                            "path": graph[u]["path"] + 1}
    try:
        print(graph[end]["path"] if graph[end]["path"] != float("inf") else -1)
    except KeyError:
        print(-1)
