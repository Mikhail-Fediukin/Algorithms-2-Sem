import time
import tracemalloc


n = int(input())  # количество дней
price = [[]]  # стоимости обедов в течение n дней
for _ in range(n):
    price.append(int(input()))


t_start = time.perf_counter()
tracemalloc.start()


M = [[float("inf") for _ in range(n+3)] for _ in range(n+1)]
M[0][1] = 0
for i in range(1, n+1):
    for j in range(1, n+2):
        if price[i] <= 100:
            M[i][j] = min(M[i-1][j] + price[i], M[i-1][j+1])
        else:
            M[i][j] = min(M[i-1][j-1] + price[i], M[i-1][j+1])
minimum = float("inf")  # минмальная сумма за все походы на обед
left = 0
for i, elem in enumerate(M[n]):
    if elem <= minimum:
        minimum = elem
        left = i
print(minimum)

dinner_days = []
i, j = n, left
while i != 0:
    if price[i] > 100:
        if M[i-1][j-1] + price[i] <= M[i-1][j+1]:
            j -= 1
        else:
            j += 1
            dinner_days.append(i)
    else:
        if M[i-1][j] + price[i] > M[i-1][j+1]:
            j += 1
            dinner_days.append(i)
    i -= 1
print(left - 1, len(dinner_days))
for days in reversed(dinner_days):
    print(days)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
