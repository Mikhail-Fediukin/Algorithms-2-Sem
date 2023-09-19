import time
import tracemalloc


paths = {0: [4, 6],
         1: [6, 8],
         2: [7, 9],
         3: [4, 8],
         4: [0, 3, 9],
         5: [],
         6: [0, 1, 7],
         7: [2, 6],
         8: [1, 3],
         9: [2, 4]}

n = int(input())


t_start = time.perf_counter()
tracemalloc.start()


M = [[1 for _ in range(10)] for _ in range(n)]
# m = n*[10*[1]] ??
for i in range(1, n):
    for j in range(10):
        M[i][j] = sum([M[i - 1][k] for k in paths[j]])
print((sum(M[n-1]) - M[n-1][0] - M[n-1][8]) % 10**9)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
