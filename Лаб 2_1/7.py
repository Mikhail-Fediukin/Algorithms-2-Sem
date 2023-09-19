import time
import tracemalloc


K, n = map(int, input().split())  # K - длина раб.дня в минутах, n - количество сапог
T = sorted(list(map(int, input().split())))  # список минут на сапог


t_start = time.perf_counter()
tracemalloc.start()


i = 0
while K - T[i] >= 0:
    K -= T[i]
    i += 1
print(i)

print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))