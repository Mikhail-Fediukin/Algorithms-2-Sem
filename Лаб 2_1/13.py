import time
import tracemalloc

n = int(input())  # количество сувениров
S = list(map(int, input().split()))  # стоимости сувенорив


t_start = time.perf_counter()
tracemalloc.start()


if sum(S) % 3 != 0:
    print(0)
else:
    share = sum(S) // 3
    S.sort(reverse=True)
    bundles = []  # итоговые пачки сувениров троих
    for i in range(3):
        bundle = []  # итоговая пачка сувениров одного
        j = 0  #
        while sum(bundle) != share:
            if sum(bundle) + S[j] <= share:
                bundle.append(S[j])
                del S[j]
            else:
                j += 1
                if j + 1 > len(S):
                    break
        bundles.append(bundle)
    print(1 if sum(bundles[0]) == sum(bundles[1]) == sum(bundles[2]) and len(S) == 0 else 0)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
