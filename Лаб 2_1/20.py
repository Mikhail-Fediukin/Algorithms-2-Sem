import time
import tracemalloc


n, k = map(int, input().split())
s = input()


t_start = time.perf_counter()
tracemalloc.start()


wrd = "|"
for i in s:  # слово с обозначеннымим промежутками между буквами
    wrd += i + "|"
count = 0  # счетчик
i = 0
nums = 0  # расхождение
for center in range(len(wrd)):
    while center - i >= 0 and center + i < len(wrd) and nums <= k:
        if wrd[center - i] != wrd[center + i]:
            nums += 1
        if wrd[center - i] != "|" and nums <= k:
            count += 1
        i += 1
    else:
        i = 0
        nums = 0
print(count)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
