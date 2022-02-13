import itertools
l: list = []

for _ in range(5):
    l.append(int(input()))

ans: int = 10 ** 6

for perm in itertools.permutations(l, 5):
    time: int = 0
    for number in perm:
        if (mod := time % 10) == 0:
            time += number
        else:
            time += number + (10-mod)

    if time < ans:
        ans = time

print(ans)