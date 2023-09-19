def pref(S):
    p = [0]*(len(S)+1)
    i, j = 1, 0
    while i < len(S):
        if S[i] == S[j]:
            p[i+1] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j]
            else:
                p[i+1] = 0
                i += 1
    return p


with open('input.txt', 'r') as infile:
    string = infile.readline().strip()
with open('output.txt', 'w') as outfile:
    print(*pref(string)[1:], file=outfile)
