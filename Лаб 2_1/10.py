import time
import tracemalloc


num, s = map(int, input().split())  # num - количество яблок, s - рост
Papples = []  # увеличивают
Napples = []  # уменьшают
for i in range(num):
    n, p = map(int, input().split())
    Papples.append([n, p-n, i + 1]) if p-n > 0 else Napples.append([n, p-n, i + 1])


t_start = time.perf_counter()
tracemalloc.start()


Papples.sort(key=lambda v: v[0])
order = []
flag = True
for apple in Papples + Napples:
    if s - apple[0] > 0:
        s += apple[1]
        order.append(apple[2])
    else:
        flag = False
        print(-1)
        break
if flag:
    print(*order)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
