import time
import tracemalloc


n = int(input())  # количество чисел
A = list(map(int, input().split()))  # список чисел


t_start = time.perf_counter()
tracemalloc.start()


s1 = sum(A)  # первая часть
s2 = 0  # вторая часть
d = []
i = n - 1
while s2 < s1:
    s1 -= A[i]
    s2 += A[i]
    d.append(i+1)
    i -= 1
if s1 != s2:
    print(-1)
else:
    print(n - 1 - i)
    print(*sorted(d))


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
