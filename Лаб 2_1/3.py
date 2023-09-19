import time
import tracemalloc


n = int(input())  # количество слотов
A = sorted(list(map(int, input().split())))  # прибыль за клик i слота
B = sorted(list(map(int, input().split())))  # количество кликов на i слот


t_start = time.perf_counter()
tracemalloc.start()


s = 0  # общий доход
for i in range(n):
    s += A[i] * B[i]
print(s)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))