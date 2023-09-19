if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = {}
    for i in range(1, n+1):
        maze[i] = {}
    for _ in range(m):
        u, v, c = map(int, input().split())
        maze[u][c] = v
        maze[v][c] = u
    n = input()
    path = list(map(int, input().split()))
    curr = 1
    flag = True
    for step in path:
        try:
            curr = maze[curr][step]
        except KeyError:
            flag = False
            break
    print("INCORRECT" if not flag else curr)
