with open('input.txt', 'r') as infile:
    initstr = infile.readline().strip().replace(" ", "")
    encoded = {}
    for i, s in enumerate(initstr):
        try:
            encoded[s].append(i)
        except Exception:
            encoded[s] = [i]
    total = 0
    for spisok in encoded.values():
        if len(spisok) > 1:
            for i, val in enumerate(spisok):
                total += val * (2*i - len(spisok) + 1)
            total -= len(spisok) * (len(spisok) - 1) // 2
with open('output.txt', 'w') as outfile:
    print(total, file=outfile)
