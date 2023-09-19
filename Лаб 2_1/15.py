import time
import tracemalloc


def changes(seq, start, end):
    if len(seq[start:end]) == 0:
        return 0, []
    if seq[end - 1] == '(' or seq[end - 1] == '[' or seq[end - 1] == '{':
        variety = [(1 + changes(seq, start, end - 1)[0], changes(seq, start, end - 1)[1] + [end - 1])]
    else:
        variety = [(1 + changes(seq, start, end - 1)[0], changes(seq, start, end - 1)[1] + [end - 1])]
        for i, bracket in enumerate(seq[start:end]):
            if bracket == '(' and seq[end - 1] == ')' or bracket == '[' and seq[end - 1] == ']' \
                    or bracket == '{' and seq[end - 1] == '}':
                one = changes(seq, start, start + i)
                two = changes(seq, start + i + 1, end - 1)
                variety.append((one[0] + two[0], one[1] + two[1]))
    improved_seq = min(variety, key=lambda para: para[0])
    return improved_seq


given_seq = input()


t_start = time.perf_counter()
tracemalloc.start()


to_del = changes(given_seq, 0, len(given_seq))[1]
new_seq = ""
for i in range(len(given_seq)):
    if i not in to_del:
        new_seq += given_seq[i]
print(new_seq)


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
