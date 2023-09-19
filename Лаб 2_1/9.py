import time
import tracemalloc


N = int(input())  # количество листов на печать
A = []  # цены за категории
count = []  # счетчик
for _ in range(7):
    A.append(int(input()))
    count.append(0)


t_start = time.perf_counter()
tracemalloc.start()


for i in range(6, -1, -1):
    count[i] = N // 10**i
    N %= 10**i

for i in range(7):
    if sum([A[x] * count[x] for x in range(i)]) >= A[i]:
        count[i] += 1
        for j in range(i):
            count[j] = 0

for i in range(6, -1, -1):
    for j in range(6, i, -1):
        if A[i] * 10**(j - i) < A[j]:
            count[i] += count[j] * int(10**(j - i))
            count[j] = 0

s = sum([A[i] * count[i] for i in range(7)])  # итоговая сумма
print(s)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
