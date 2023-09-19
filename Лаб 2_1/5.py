import time
import tracemalloc


n = int(input())


t_start = time.perf_counter()
tracemalloc.start()


i = 0  # количество детей
s = 0  # счетчик конфет на человека
seq = []  # последовательность распределенных конфет
while s < n:
    i += 1
    s += i
    seq.append(i)
if s == n:
    print(i)
    print(*seq)
else:
    print(i - 1)
    print(*seq[:-2], i - 1 + n - sum(seq[:-1]))


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
