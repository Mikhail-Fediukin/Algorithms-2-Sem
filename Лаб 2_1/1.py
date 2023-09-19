import time
import tracemalloc

n, W = map(int, input().split())  # n - количество предметов, W - вместимость сумки
items = []  # предметы
for _ in range(n):
    items.append(tuple(map(int, input().split())))


t_start = time.perf_counter()
tracemalloc.start()


items.sort(key=lambda val: val[1]/val[0])
v, i = 0.0, 0  # v - итоговая стоимость добычи, i - счетчик
while W > 0:
    if items[i][1] <= W:
        W -= items[i][1]
        v += items[i][0]
        i += 1
    else:
        v += W * (items[i][0]/items[i][1])
        W = 0
print(round(v, 3))


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
