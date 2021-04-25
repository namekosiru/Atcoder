n = int(input())
s = list(input())
q = int(input())

flip = 0

for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1

    if t == 2:
        flip += 1
        # tmp = s[li[1]-1]
        # s[li[1]-1] = s[li[2]-1]
        # s[li[2]-1] = tmp
    elif t == 1:
        if flip % 2 == 0:
            a, b = b, a
        else:
            if a >= n:
                a -= n
                b -= n
            elif  b >= n and a < n:
                a += n
                b -= n
            else:
                a += n
                b += n

        s[a], s[b] = s[b], s[a]

if flip % 2 == 0:
    print(*s, sep="")
else:
    s = s[n:] + s[:n]
    print(*s, sep="")

