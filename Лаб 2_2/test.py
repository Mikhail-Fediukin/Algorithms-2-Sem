import time
import tracemalloc
import tree_struct_AVL


def time_memory(function):
    def wrapper():
        t_start = time.perf_counter()
        tracemalloc.start()
        function()
        print("Time:", time.perf_counter() - t_start)
        mc, mp = tracemalloc.get_traced_memory()
        print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
    return wrapper


