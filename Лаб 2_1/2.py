import time
import tracemalloc


d = int(input())  # расстояние
m = int(input())  # может проехать
n = int(input())  # количество заправок
stop = list(map(int, input().split()))  # возможные остановки


t_start = time.perf_counter()
tracemalloc.start()


stop = [m] + stop + [d]
passed = 0  # пройденный путь
s = 0  # количество заправок
flag = True
for i, station in enumerate(stop):
    if station - stop[i - 1] > m:
        print(-1)
        flag = False
        break
    if station - passed > m:
        passed = stop[i - 1]
        s += 1
if flag:
    print(s)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
