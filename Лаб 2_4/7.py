from random import randint


with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        line = infile.readline().strip()
        while len(line) != 0:
            s, t = line.split()

            m1 = 10**9 + 7
            m2 = 10**9 + 9
            x = randint(1, 10**9)
            hashes_s_1 = [0]
            hashes_s_2 = [0]
            hashes_t_1 = [0]
            hashes_t_2 = [0]
            for i, letter in enumerate(s):
                hashes_s_1.append((x * hashes_s_1[i] + ord(letter)) % m1)
                hashes_s_2.append((x * hashes_s_2[i] + ord(letter)) % m2)
            for i, letter in enumerate(t):
                hashes_t_1.append((x * hashes_t_1[i] + ord(letter)) % m1)
                hashes_t_2.append((x * hashes_t_2[i] + ord(letter)) % m2)

            dict_with_hashes = {}
            for k in range(1, min(len(s), len(t)) + 1):
                dict_with_hashes[k] = {"s1": [], "t1": [], "s2": [], "t2": []}
                for i in range(len(hashes_s_1) - k):
                    dict_with_hashes[k]["s1"].append((hashes_s_1[i + k] - x**k * hashes_s_1[i]) % m1)
                    dict_with_hashes[k]["s2"].append((hashes_s_2[i + k] - x ** k * hashes_s_2[i]) % m2)
                for i in range(len(hashes_t_1) - k):
                    dict_with_hashes[k]["t1"].append((hashes_t_1[i + k] - x**k * hashes_t_1[i]) % m1)
                    dict_with_hashes[k]["t2"].append((hashes_t_2[i + k] - x ** k * hashes_t_2[i]) % m2)

            flag = False
            for k in range(min(len(s), len(t)), 0, -1):
                current_dict = dict_with_hashes[k]
                for s_i, s_hash in enumerate(current_dict["s1"]):
                    for t_i, t_hash in enumerate(current_dict["t1"]):
                        if s_hash == t_hash:
                            if current_dict["s2"][s_i] == current_dict["t2"][t_i]:
                                print(s_i, t_i, k, file=outfile)
                                flag = True
                                break
                    if flag:
                        break
                if flag:
                    break

            if not flag:
                print(0, 0, 0, file=outfile)
            line = infile.readline().strip()
