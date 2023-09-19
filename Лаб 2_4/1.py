with open('input.txt', 'r') as infile:
    sub = infile.readline().strip()
    initstr = infile.readline().strip()
    found_ind = []
    for i in range(len(initstr) - len(sub) + 1):
        if initstr[i:i+len(sub)] == sub:
            found_ind.append(i+1)
with open('output.txt', 'w') as outfile:
    print(len(found_ind), file=outfile)
    print(*found_ind, file=outfile)
