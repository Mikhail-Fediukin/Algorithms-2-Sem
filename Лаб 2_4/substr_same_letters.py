string = input()
letters = {}
for i, let in enumerate(string):
    try:
        letters[let].append(i)
    except Exception:
        letters[let] = [i]
mx = 0
for spisok in letters.values():
    if spisok[-1] - spisok[0] > mx:
        mx = spisok[-1] - spisok[0]
print(mx)
