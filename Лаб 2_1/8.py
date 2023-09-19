import time
import tracemalloc


N = int(input())  # количество заявок
slots = []  # интервалы занятий
for _ in range(N):
    a, b = map(int, input().split())
    slots.append((a, b))


t_start = time.perf_counter()
tracemalloc.start()


slots = sorted(slots, key=lambda v: (v[1], v[0]))
cur_slot = slots[0][1]  # конец предыдущего временного слота
sch = 1  # количество предметов (расписание)
for slot in slots[1:]:
    if slot[0] >= cur_slot:
        sch += 1
        cur_slot = slot[1]
print(sch)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
