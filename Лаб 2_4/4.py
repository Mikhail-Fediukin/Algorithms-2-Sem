from random import randint


with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        string = infile.readline().strip()
        n = int(infile.readline())
        m1 = 10**9 + 7
        m2 = 10**9 + 9
        x = randint(1, 10**9)
        hashes1 = [0]
        hashes2 = [0]
        for i, s in enumerate(string):
            hashes1.append((x * hashes1[i] + ord(s)) % m1)
            hashes2.append((x * hashes2[i] + ord(s)) % m2)
        for _ in range(n):
            a, b, l = map(int, infile.readline().split())
            hasha1 = hashes1[a + l] - x**l * hashes1[a]
            hashb1 = hashes1[b + l] - x**l * hashes1[b]
            if hasha1 % m1 == hashb1 % m1:
                hasha2 = hashes2[a + l] - x ** l * hashes2[a]
                hashb2 = hashes2[b + l] - x ** l * hashes2[b]
                if hasha2 % m2 == hashb2 % m2:
                    print("Yes", file=outfile)
                    continue
            print('No', file=outfile)
