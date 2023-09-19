import time
import tracemalloc


Ranks = {'S': 0,
         'C': 1,
         'D': 2,
         'H': 3}

Suits = {'6': 0,
         '7': 1,
         '8': 2,
         '9': 3,
         'T': 4,
         'J': 5,
         'Q': 6,
         'K': 7,
         'A': 8}


def durak(trump_card, me, opponent):
    m = [[0 for _ in range(9)] for _ in range(4)]
    for item in me:
        m[Ranks[item[1]]][Suits[item[0]]] = 1
    for item in opponent:
        row, col = Ranks[item[1]], Suits[item[0]]
        flag = True
        for j in range(col, 9):
            if m[row][j] != 0:
                m[row][j] = 0
                flag = False
                break
        if flag and row != Ranks[trump_card]:
            flag = True
            row, col = Ranks[trump_card], 0
            for j in range(col, 9):
                if m[row][j] != 0:
                    m[row][j] = 0
                    flag = False
                    break
        if flag:
            return "NO"
    return "YES"


n, m, trump = input().split()
my_deck = list(input().split())
opp_deck = list(input().split())


t_start = time.perf_counter()
tracemalloc.start()


print(durak(trump, my_deck, opp_deck))


print("Time:", time.perf_counter() - t_start)
mc, mp = tracemalloc.get_traced_memory()
print("Current memory %f KiB, peak %f KiB" % (mc / 1024, mp / 1024))
