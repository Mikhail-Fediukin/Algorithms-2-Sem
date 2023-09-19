import time
import tracemalloc


n = int(input())  # количество чисел
A = list(input().split())  # список чисел


t_start = time.perf_counter()
tracemalloc.start()


L = len(max(A, key=len))
print("".join(reversed(sorted(A, key=lambda i: i + i[-1]*(L - len(i))))))


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
