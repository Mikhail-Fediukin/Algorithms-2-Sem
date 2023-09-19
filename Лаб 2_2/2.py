def get_h(n, h1, h0):
    return n*h1 - (n-1)*h0 + n*(n-1)


with open('input.txt', 'r', encoding='utf-8') as file:
    number, h0 = file.readline().split()
number, h0 = int(number), float(h0)
mn = 10**9
left, right = 0, h0
mid = (left + right) / 2
while mid != left and mid != right:
    h1 = mid
    flag = True
    for n in range(2, number):
        if get_h(n, h1, h0) < 0:
            flag = False
            break
    if flag:
        right = mid
        curr = get_h(number-1, h1, h0)
        if curr < mn:
            mn = curr
    else:
        left = mid
    mid = (left + right) / 2
with open('output.txt', 'w', encoding='utf-8') as file:
    print(mn, file=file)

