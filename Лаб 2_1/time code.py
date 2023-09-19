import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
