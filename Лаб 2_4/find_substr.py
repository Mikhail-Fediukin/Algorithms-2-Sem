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


initstring = input().strip()
substring = input().strip()
mystr = substring + '#' + initstring
prefixes = pref(mystr)
length = len(substring)
found_ind = []
for i, prefix in enumerate(prefixes[length + 1:]):
    if prefix == length:
        found_ind.append(i - length)
print(*found_ind)
